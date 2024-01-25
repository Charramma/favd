<style lang="less">
	@import './login.less'; // 导入样式文件
</style>

<template>
	<div class="login">
		<div class="login-con">
			<Card icon="log-in" title="欢迎登录" :bordered="false">
				<div class="form-con">
					<!-- 引用一个名为login-form的子组件,监听其触发的on-success-valid事件，事件会调用handleSubmit方法 -->
					<!-- login-form路径：src/comnents/login-form/login-form.vue -->
					<login-form @on-success-valid="handleSubmit"></login-form>
					<p class='login-tip' v-if="errorMessage"><span style="color: red;">{{ errorMessage }}</span></p>
				</div>
			</Card>
		</div>
	</div>
</template>

<script>
	import LoginForm from '_c/login-form' // 引入子组件
	import {
		mapActions
	} from 'vuex' // 从Vuex引入mapActions辅助函数
	export default {
		components: {
			LoginForm // 注册子组件
		},
		data() {
			return {
				errorMessage: ''
			}
		},
		methods: {
			...mapActions([
				'handleLogin',
				'getUserInfo'
			]),
			// 用于处理子组件login-form触发的成功验证事件
			handleSubmit({
				userName,
				password
			}) {
				// 调用handleLogin action进行登录
				// 然后在登录成功后调用getUserInfo action获取用户信息
				// this.handleLogin({ userName, password }).then(res => {
				//   this.getUserInfo().then(res => {
				//     this.$router.push({	// 最后使用$router进行路由导航跳转到配置中定义的首页。
				//       name: this.$config.homeName
				//     })
				//   })
				// })
				this.$store.dispatch('handleLogin', {
					userName,
					password
				}).then(() => {
					this.getUserInfo().then(res => {
						// 登录成功提示
						this.$Message.success('登录成功'),
						this.$router.push({ // 最后使用$router进行路由导航跳转到配置中定义的首页。
								name: this.$config.homeName
							})
					})
				}).catch((error) => {
					this.errorMessage = error;
					console.error('Login failed', 'error');
				})
			},
		}
	}
</script>

<style>

</style>