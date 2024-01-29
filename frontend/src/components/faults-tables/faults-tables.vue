<template>
	<div>
		<!-- 搜索框及新建故障按钮 -->
		<div class="search-con search-con-top">
			<Select v-model="searchKey" class="search-col" style="width: 200px;">
				<Option v-for="item in searchTypes" :value="item.value" :key="item.value">{{ item.lable }}</Option>
			</Select>
			<Input @on-change="handleClear" clearable placeholder="输入关键字搜索" class="search-input" v-model="searchValue"
				style="width: 200px;" />
			<Button class="search-btn" type="primary">搜索</Button>

			<Button type="success" @click="addFaultMoal=true">新建故障</Button>
			<!-- 新建故障对话框 -->
			<Modal v-model="addFaultMoal" :mask-closable="false" title="新建故障: " width="550px" class-name="vertical-center-modal">
				<Form :model="addFaultForm" :label-width="80" ref="addFaultForm" :rules="addFaultFormRule">
					<FormItem label="故障名称: " prop="faultName">
						<Input v-model="addFaultForm.faultName" placeholder="请输入故障名称"></Input>
					</FormItem>
					<FormItem label="故障状态: " prop="faultStatus">
						<Select v-model="addFaultForm.faultStatus">
							<Option value="处理中">处理中</Option>
							<Option value="已关闭">已关闭</Option>
						</Select>
					</FormItem>
					<FormItem label="故障等级: " prop="faultLevel">
						<Select v-model="addFaultForm.faultLevel">
							<Option value="一级故障">一级故障</Option>
							<Option value="二级故障">二级故障</Option>
							<Option value="三级故障">三级故障</Option>
							<Option value="四级故障">四级故障</Option>
							<Option value="五级故障">五级故障</Option>
						</Select>
					</FormItem>
					<FormItem label="责任人" prop="responsible">
						<Input v-model="addFaultForm.responsible" placeholder="故障责任人"></Input>
					</FormItem>
					<FormItem label="故障处理人" prop="handler">
						<Input v-model="addFaultForm.handler" placeholder="故障处理人"></Input>
					</FormItem>
					<FormItem label="开始时间" prop="startTime">
						<DatePicker type="datetime" placeholder="选择故障开始日期和时间" style="width: 400px" v-model="addFaultForm.startTime"
							format="yyyy-MM-dd HH:mm:ss">
						</DatePicker>
					</FormItem>
					<FormItem label="结束时间" prop="endTime">
						<DatePicker type="datetime" placeholder="选择故障处理完成日期和时间" style="width: 400px" v-model="addFaultForm.endTime"
							format="yyyy-MM-dd HH:mm:ss">
						</DatePicker>
					</FormItem>
					<FormItem label="故障原因" prop="causeOfFault">
						<Input v-model="addFaultForm.causeOfFault" type="textarea" :autosize="{minRows: 2,maxRows: 5}"
							placeholder="请描述一下本次故障原因" maxlength=500></Input>
					</FormItem>
					<FormItem label="故障总结" prop="summaryOfFault">
						<Input v-model="addFaultForm.summaryOfFault" type="textarea" :autosize="{minRows: 2,maxRows: 5}"
							placeholder="请对本次故障进行总结" maxlength=500></Input>
					</FormItem>
					<FormItem>
						<Button type="primary" @click="AddError('addFaultForm')">提交</Button>
						<Button @click="handleFormReset('addFaultForm')" style="margin-left: 8px">重置</Button>
					</FormItem>
				</Form>
				<div slot="footer">
					<!-- 此处仅为了禁用默认的确认和取消按钮 -->
				</div>
			</Modal>

		</div>
		<!-- <br /> -->
		<!-- 故障清单 表格 -->
		<Table border :columns="insideTableHeader" :data="insideTableData"></Table>
		<br />
    <!-- 分页 -->
		<Page :model-value="insideTablePage" :total="insideTableDataCount" show-total @on-change="handlePageChange"></Page>
	</div>
</template>

<script>
	import {
		mapActions
	} from 'vuex';
import ops_tools from '../../store/module/ops_tools';
	export default {
		name: 'FaultsTables',
		data() {
			return {
				// 新建故障 对话框数据
				addFaultMoal: false, // 是否显示对话框
				addFaultForm: {
					faultName: "", // 故障名称
					faultStatus: "", // 故障状态,
					faultLevel: "", // 故障等级
					responsible: "", // 责任人
					handler: "", // 处理人员
					startTime: "", // 开始时间
					endTime: "", // 结束时间
					causeOfFault: "", // 故障原因
					summaryOfFault: "", //故障总结
				},
				addFaultFormRule: { // 表单验证规则
					faultName: [{
						required: true,
						message: '故障名称不能为空',
						trigger: 'blur'
					}],
					faultStatus: [{
						required: true,
						message: '故障状态不能为空',
						trigger: 'change'
					}],
					faultLevel: [{
						required: true,
						message: '故障等级不能为空',
						trigger: 'change'
					}],
					responsible: [{
						required: true,
						message: '故障责任人不能为空',
						trigger: 'blur'
					}],
				},
				// 新建故障数据结束

				searchValue: '', // 搜索关键字
				searchKey: '', // 搜索类别
				searchTypes: [{
						value: 'errorName',
						lable: '故障名称'
					},
					{
						value: 'errorStatus',
						lable: '故障状态'
					},
					{
						value: 'errorLevel',
						lable: '故障级别'
					},
					{
						value: 'responsible',
						lable: '故障责任人'
					}
				],
				// 表头
				insideTableHeader: [{
						title: '故障名称',
						key: 'falut_name',
						sortable: true,
						align: "center"
					},
					{
						title: '故障状态',
						key: 'fault_status',
						sortable: true,
						align: "center"
					},
					{
						title: '故障级别',
						key: 'fault_level',
						sortable: true,
						align: "center"
					},
					{
						title: '故障责任人',
						key: 'responsible',
						sortable: true,
						align: "center"
					},
          {
            title: '处理人',
            key: 'handler',
            align: "center"
          },
					{
						title: '故障报告',
						key: 'errorReport',
						width: 150,
						align: 'center',
						render: (h, params) => {
							return h('div', [
								h('Button', {
									props: {
										type: 'primary',
										size: 'small'
									},
									style: {
										marginRight: '5px'
									},
									on: {
										click: () => {
											this.showErrorReport(params.index)
										}
									}
								}, '查看报告')
							])
						}
					},
					{
						title: '开始时间',
						key: 'start_time',
						sortable: true,
						align: "center"
					},
					{
						title: '结束时间',
						key: 'end_time',
						sortable: true,
						align: "center"
					},
					{
						title: '操作',
						key: 'action',
						width: 150,
						align: 'center',
						render: (h, params) => {
							return h('div', [
								h('Button', {
									props: {
										type: 'primary',
										size: 'small'
									},
									style: {
										marginRight: '5px'
									},
									on: {
										click: () => {
											this.editError(params.index)
										}
									}
								}, '编辑'),
								h('Button', {
									props: {
										type: 'error',
										size: 'small'
									},
									on: {
										click: () => {
											this.removeError(params.index)
										}
									}
								}, '删除')
							]);
						}
					}
				],
				insideTableData: [], // 表格数据
        insideTablePage: "1", // 表格页码
        insideTableDataCount: "", // 表格总页码
			}
		},
    mounted() {
      // 挂载组件时立即获取表格数据
      this.handleTableData();
    },
		methods: {
			...mapActions([
				'handleAddFault', 'handleGetFaults', 'handleDelFault'
			]),
      // 获取表格数据
      handleTableData () {
        console.log(this.insideTablePage)
        this.handleGetFaults(this.insideTablePage).then(() => {
          this.insideTableData = this.$store.getters.getFaultsInfo;
          this.insideTableDataCount = this.$store.getters.getFaultCount;
        }).catch(err => {
					this.$Message.error(err);
					console.error("获取故障信息失败: ", err);
				});
      },
      // 分页器页码改变时触发的方法
      handlePageChange(page) {
        this.insideTablePage = page;
        this.handleTableData();
      },
			// 编辑故障
			editError(index) {

			},
			// 删除故障
			removeError(index) {
        this.handleDelFault(this.insideTableData[index].fault_id).then(() => {
          this.$Message.success('删除故障信息成功');
        }).catch(err => {
          this.$Message.error(err);
          console.error('删除故障信息失败', err);
        })
        // console.log(this.insideTableData[index].fault_id);
			},
      handleClear() {

      },
			// 提交故障
			AddError(name) {
				this.$refs[name].validate((valid) => {
					if (valid) {
						// 将ISO格式的时间转换为本地日期时间格式
						this.addFaultForm.startTime = this.formatDate(this.addFaultForm.startTime);
						this.addFaultForm.endTime = this.formatDate(this.addFaultForm.endTime);

						this.handleAddFault(this.addFaultForm).then(() => {
							this.$Message.success('提交成功');
							this.$refs.addFaultForm.resetFields(); // 重置表单数据
							this.addFaultMoal = false; // 关闭对话框
						}).catch(err => {
							console.log(err)
							this.$Message.error(err.response.data.message)
						})
					} else {
						this.$Message.error('缺少必要参数!');
					}
				})
			},
			// 重置表单
			handleFormReset(name) {
				this.$refs[name].resetFields();
			},
			// 日期时间格式转换
			formatDate(dateString) {
				const date = new Date(dateString);
				const year = date.getFullYear();
				const month = String(date.getMonth() + 1).padStart(2, '0');
				const day = String(date.getDate()).padStart(2, '0');
				const hours = String(date.getHours()).padStart(2, '0');
				const minutes = String(date.getMinutes()).padStart(2, '0');
				const seconds = String(date.getSeconds()).padStart(2, '0');
				return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
			},
		},
	}
</script>

<style>
	div.search-con-top>* {
		margin-right: 5px;
    margin-bottom: 5px;
	}

	.vertical-center-modal {
		display: flex;
		align-items: center;
		justify-content: center;

		.ivu-modal {
			top: 0;
		}
	}
</style>
