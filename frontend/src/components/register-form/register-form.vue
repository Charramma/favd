<template>
	<Form ref="RegisterForm" :model="form" :rules="rules" @keydown.enter.native="handleSubmit">
		<!-- 用户名输入表单 -->
		<FormItem prop="userName">
			<Input v-model="form.userName" placeholder="请输入用户名">
			<span slot="prepend"> <!-- 图标 -->
				<Icon :size="16" type="ios-person"></Icon>
			</span>
			</Input>
		</FormItem>
		<!-- 邮箱输入表单 -->
		<FormItem prop="email">
			<Input v-model="form.email" placeholder="请输入邮箱">
			<span slot="prepend">
				<Icon :size="16" type="ios-mail-outline"></Icon>
			</span>
			</Input>
		</FormItem>
		<!-- 密码输入表单 -->
		<FormItem prop="password">
			<Input type="password" v-model="form.password" placeholder="请输入密码">
			<span slot="prepend">
				<Icon :size="14" type="md-lock"></Icon>
			</span>
			</Input>
		</FormItem>
		<!-- 再次输入密码 -->
		<FormItem prop="passwordCheck">
			<Input type="password" v-model="form.passwordCheck" placeholder="请再次输入密码">
			<span slot="prepend">
				<Icon :size="14" type="md-lock"></Icon>
			</span>
			</Input>
		</FormItem>
		<!-- 注册按钮 -->
		<FormItem>
			<Button @click="handleSubmit" type="primary" long>注册</Button>
		</FormItem>
	</Form>
</template>

<script>
	export default {
		name: 'RegisterForm',
		props: {
			userNameRules: {
				type: Array,
				default: () => {
					return [{
						required: true,
						message: '账号不能为空',
						trigger: 'blur'
					}]
				}
			},
			emailRules: {
				type: Array,
				default: () => {
					return [{
							required: true,
							message: '邮箱不能为空',
							trigger: 'blur'
						},
						{
							type: 'email',
							message: '请输入正确的邮箱格式',
							trigger: ['blur', 'change']
						}
					]
				}
			},
			passwordRules: {
				type: Array,
				default: () => {
					return [{
							required: true,
							message: '密码不能为空',
							trigger: 'blur'
						},
						{
							min: 8,
							message: '密码长度不能少于8位',
							trigger: 'blur'
						},
						{
							pattern: /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]+$/,
							message: '密码必须包含大小写字母、数字和特殊符号',
							trigger: 'blur'
						}
					]
				}
			},
			passwordCheckRules: {
				type: Array,
				default: () => {
					return [{
						required: true,
						message: '请再次输入密码',
						trigger: 'blur'
					}]
				}
			}
		},
		data() {
			return {
				form: {
					userName: '',
					email: '',
					password: '',
					passwordCheck: ''
				}
			}
		},
		computed: {
			rules() {
				return {
					userName: this.userNameRules,
					email: this.emailRules,
					password: this.passwordRules,
					passwordCheck: [
						...this.passwordRules,
						{
							validator: this.validatePasswordCheck,
							trigger: ['blur', 'change']
						}
					],
				}
			}
		},
		methods: {
			// 验证二次输入的密码是否正确
			validatePasswordCheck(rule, value, callback) {
				if (value !== this.form.password) {
					callback(new Error('两次输入的密码不一致'));
				} else {
					callback();
				}
			},
			// 将用户名、邮箱、密码传递给父组件
			handleSubmit() {
				this.$refs.RegisterForm.validate((valid) => {
					if (valid) {
						this.$emit('on-success-valid', {
							userName: this.form.userName,
							email: this.form.email,
							password: this.form.password
						})
					}
				})
			}
		}
	}
</script>