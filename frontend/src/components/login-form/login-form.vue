<template>
	<Form ref="loginForm" :model="form" :rules="rules" @keydown.enter.native="handleSubmit">
		<!-- 用户名输入表单 -->
		<FormItem prop="userName">
			<Input v-model="form.userName" placeholder="请输入邮箱">
			<span slot="prepend"> <!-- 图标 -->
				<Icon :size="16" type="ios-person"></Icon>
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
		<!-- 登录按钮和注册按钮 -->
		<FormItem class="button-group">
			<Row :gutter="16"> <!-- 设置栅格之间的间距为 16 像素 -->
				<i-col span="12">
					<Button @click="handleSubmit" type="primary" long>登录</Button>
				</i-col>
				<i-col span="12">
					<Button @click="navigateToRegister" type="info" long>注册</Button>
				</i-col>
			</Row>
		</FormItem>
	</Form>
</template>
<script>
	export default {
		name: 'LoginForm',
		props: {
			userNameRules: {
				type: Array,
				default: () => {
					return [{
							required: true,
							message: '邮箱地址不能为空',
							trigger: 'blur'
						},
						{
							type: 'email',
							message: '请输入正确的邮箱格式',
							trigger: 'blur'
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
					}]
				}
			}
		},
		data() {
			return {
				form: {
					userName: '',
					password: ''
				}
			}
		},
		computed: {
			rules() {
				return {
					userName: this.userNameRules,
					password: this.passwordRules
				}
			}
		},
		methods: {
			handleSubmit() {
				this.$refs.loginForm.validate((valid) => {
					if (valid) {
						this.$emit('on-success-valid', {
							userName: this.form.userName,
							password: this.form.password
						})
					}
				})
			},
			navigateToRegister() {
				this.$router.push('/register')
			}
		}
	}
</script>