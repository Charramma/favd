<style lang="less">
	@import './register.less';
</style>

<template>
	<div class="register">
		<div class="register-con">
			<Card icon="log-in" title="注册" :bordered="false">
				<div class="form-con">
					<register-form @on-success-valid="handleSubmit"></register-form>
				</div>
			</Card>
		</div>
	</div>
</template>

<script>
	import RegisterForm from '_c/register-form' // 引入子组件
	import {
		mapActions
	} from 'vuex'
	export default {
		components: {
			RegisterForm
		},

		methods: {
			...mapActions([
				'handleRegister'
			]),

			handleSubmit({
				userName,
				email,
				password
			}) {
				this.handleRegister({
					userName,
					email,
					password
				}).then(res => {
					// 注册成功提示
					this.$Message.success('注册成功'),
					this.$router.push({
						// 跳转到登录界面
						name: this.$config.loginPage
					})
				})
			}
		}
	}
</script>

<style>

</style>