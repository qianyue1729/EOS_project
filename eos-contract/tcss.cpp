#include <eosio/eosio.hpp>
#include <eosio/print.hpp>
#include <eosio/transaction.hpp>
#include <eosio/time.hpp>
#include <eosio/crypto.hpp>

using namespace eosio;

class [[eosio::contract]] tcss : public contract {
// 公开
public:
    using contract::contract;

    // 1. 上传文件哈希值
    [[eosio::action]]
    void upload(name user, std::string file_hash, std::string file_name, std::string file_str) { // 传入:合约用户名、文件哈希值、文件名、文件字符串形式
        // 验证账户是否为合约用户本人
        require_auth(user);
        // EOSIO内置的get_self()函数，目的是见擦汗调用者是否为合约自身，防止未经授权的外部实体调用
        hash_table file_hash_table(get_self(), get_self().value);
        // 根据文件哈希值去查找有没有相同的文件哈希，如果相同，则itr会指向该记录，如果没有，则会指向最后一个记录，即file_hash_table.end()
        auto itr = file_hash_table.find(filehash::file_hash_value(file_hash));
        // 如果itr没有指向end，说明找到了对应的记录，返回该文件哈希已经存在，并终止该合约
        check(itr == file_hash_table.end(), "This file hash already exists in our system.");
        // 使用emplace方法插入合约用户与记录
        file_hash_table.emplace(user, [&](auto& row) {
            row.file_hash = file_hash;
            row.file_name = file_name;
            row.file_str = file_str;
            row.uploader = user;
            row.timestamp = current_time_point();
        });

        print("This file hash has already uploaded successfully!");
    }

    // 2. 验证文件哈希值
    [[eosio::action]]
    void verify(name user, std::string file_hash) {
        // 验证账户是否为合约用户本人
        require_auth(user);

        hash_table file_hash_table(get_self(), get_self().value);
        // 验证该记录是否已经存在链上
        auto itr = file_hash_table.find(filehash::file_hash_value(file_hash));
        // 需要itr最后不指向end，否则说明其文件哈希值没有存在表中
        check(itr != file_hash_table.end(), "File hash not found");

        print("The trust storage system has verified this file hash: ", file_hash);
    }
// 该合约使用的数据结构，其它合约不能调用
private:
    // 使用eosio的table类型数据结构
    struct [[eosio::table]] filehash {
        std::string file_hash; //文件哈希值
        std::string file_name; // 文件名
        std::string file_str; // 文件字符串形式
        name uploader; // 文件上传者
        time_point timestamp; //时间戳
        // 返回每一行的主键值，EOSIO的multi_index表每一行都需要通过唯一的主键进行标识
        uint64_t primary_key() const { 
            return file_hash_value(file_hash); 
        }
        // file_hash_value函数可以将一个文件的哈希字符串转化为uint64_t类型，作为表的主键（SHA-256输出256位，仅需要64位作为主键）
        static uint64_t file_hash_value(const std::string& str) {
            checksum256 result;
            result = sha256(const_cast<char*>(str.c_str()), str.size());
            return result.extract_as_byte_array()[0];
        }
    };
    // 将文件哈希类型命名为hash_table，创建表与主键
    using hash_table = eosio::multi_index<"filehash"_n, filehash>;
};

EOSIO_DISPATCH(tcss, (upload)(verify))
