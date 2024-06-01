<template>
    <el-container class="container">
      <el-header>
        <h3>已存入数据列表表</h3>
      </el-header>
      <el-main>
        <el-table :data="tableData" style="width: 100%">
          <el-table-column prop="id" label="序号" width="50"></el-table-column>
          <el-table-column prop="content" label="存证内容"></el-table-column>
          <el-table-column prop="unit" label="存证单位"></el-table-column>
          <el-table-column prop="person" label="存证人"></el-table-column>
          <el-table-column prop="source" label="数据来源"></el-table-column>
          <el-table-column prop="date" label="存证时间"></el-table-column>
          <el-table-column prop="block" label="存入区块"></el-table-column>
          <el-table-column prop="status" label="存入状态"></el-table-column>
          <el-table-column prop="hash" label="数据Hash"></el-table-column>
          <el-table-column label="操作" width="100">
            <template slot-scope="scope">
              <el-button size="mini" type="primary" @click="handleDetails(scope.row)">详情</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-pagination
          background
          layout="prev, pager, next"
          :total="total"
          :page-size="pageSize"
          :current-page="currentPage"
          @current-change="handlePageChange">
        </el-pagination>
      </el-main>
    </el-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tableData: [
          { id: 1, content: '凶杀案现场', unit: '公安局', person: '何鲁', source: '照片', date: '2019.5.11', block: '2019-08-01', status: '已存入', hash: '83eeec5f8...' },
          { id: 2, content: '电信诈骗', unit: '检察院', person: '李肖', source: '银行监控', date: '2016.01.23', block: '2019-08-01', status: '已存入', hash: '372e5b28...' },
          { id: 3, content: '死者DNA', unit: '公安局', person: '何鲁', source: 'DNA鉴定', date: '2019.3.11', block: '2019-08-01', status: '已存入', hash: 'c30bae2c...' },
          { id: 4, content: '财产抵押', unit: '公安局', person: '何鲁', source: '照片', date: '2019.5.15', block: '2019-08-01', status: '已存入', hash: '2e7c4f12d...' },
          { id: 5, content: '杀人案证据', unit: '公安局', person: '安柏杰', source: '照片', date: '2019.3.25', block: '2019-08-01', status: '已存入', hash: '234627a0...' },
          { id: 6, content: '受贿证据', unit: '检察院', person: '李肖', source: '照片', date: '2019.3.10', block: '2019-08-01', status: '已存入', hash: 'ee1fdf285...' },
          { id: 7, content: '微信诈骗', unit: '检察院', person: '张果果', source: '手机截图', date: '2019.02.22', block: '2019-08-01', status: '已存入', hash: 'f69804c07...' },
          { id: 8, content: '合同欺诈', unit: '法院', person: '郑爱国', source: '照片', date: '2019.02.15', block: '2019-08-01', status: '已存入', hash: '403a01a3...' },
          { id: 9, content: '短信诈骗', unit: '检察院', person: '何贝', source: '手机截图', date: '2019.01.12', block: '2019-08-01', status: '已存入', hash: '937f82005...' },
          { id: 10, content: '版权侵犯', unit: '司法部门', person: '李强', source: '法院', date: '2018-12-01', block: '2019-08-01', status: '已存入', hash: '66bfdf8a7...' }
        ],
        total: 10,
        pageSize: 10,
        currentPage: 1
      };
    },
    methods: {
      handleDetails(row) {
        console.log('Details clicked:', row);
        // Add your logic to handle the details button click
      },
      handlePageChange(page) {
        this.currentPage = page;
        // Add your logic to handle the page change
      }
    }
  };
  </script>
  
  <style>
.container {
  max-width: 1200px;
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,0.1);
}
  .el-header {
    background-color: #f5f5f5;
    padding: 10px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
  }
  .el-main {
    padding: 20px;
  }
  .el-table th, .el-table td {
    text-align: center;
  }
  .el-pagination {
    margin-top: 20px;
    text-align: center;
  }
  </style>
  