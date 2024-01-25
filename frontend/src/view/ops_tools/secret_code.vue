<template>
	<div>
		<!-- 随机密码生成 -->
		<Card>
			<Alert>本系统不会记录您的随机密码，请你妥善保存。</Alert>
			<p slot="title">随机密码</p>
			<Row>
				要使用的字符：
				<CheckboxGroup v-model="characterCheck">
					<Checkbox label="ABCDEFGHIJKLMNOPQRSTUVWXYZ"><span>A-Z</span></Checkbox>
					<Checkbox label="abcdefghijklmnopqrstuvwxyz"><span>a-z</span></Checkbox>
					<Checkbox label="0123456789"><span>0-9</span></Checkbox>
					<Checkbox label="!@#$%^"><span>!@#$%^</span></Checkbox>
				</CheckboxGroup>
			</Row>
			<br />
			<Row>
				<p>密码长度：</p>
				<Input v-model="passLength" placeholder="支持生成长度为6-32位的随机密码" style="width: 200px"></Input>
			</Row>
			<br />
			<Row>
				<Button type="primary" @click="generatePassword">生成密码</Button>
			</Row>
			<h2 v-if="randomPass">{{ randomPass }}</h2>
		</Card>
		<br />
		<!-- AES加密解密 -->
		<Card>
			<p slot="title">AES加密解密</p>
			<Alert>提醒：AES加密所用到的Key在后端代码里面，前端不展示，使用人员可自行修改，防止被破解！</Alert>
			<Row type="flex" justify="space-around" align="middle">
				<Col span="10">
				<Input v-model="plain_text" type="textarea" placeholder="输入要加密的内容..." :rows="5"></Input>
				</Col>
				<Col span="4" type="flex" justify="center" align="middle">
				<Button type="info" @click="encryptText">点击加密</Button><br />
				<Button type="primary" @click="decryptText" style="margin-top: 10px;">点击解密</Button>
				</Col>
				<Col span="10">
				<Input v-model="ciphertext" type="textarea" placeholder="输入要解密的内容..." :rows="5"></Input>
				</Col>
			</Row>
		</Card>
	</div>
</template>

<script>
	import {
		mapState,
		mapGetters,
		mapActions
	} from 'vuex';
	export default {
		data() {
			return {
				plain_text: "",
				ciphertext: "",
				passLength: 16,
				characterCheck: ["0123456789"],
				randomPass: ""
			};
		},
		computed: {
			...mapState(['ciphertext', 'plain_text', 'random_pass']),
			// 使用 mapGetters 获取 state 的值
			...mapGetters(['getCiphertext', 'getPlaintext', 'getRandompass']),
			
			character: function() {
				return this.characterCheck.join('')
			}
		},
		methods: {
			...mapActions(['handleEncrypt', 'handleDecrypt', 'handleRandomPassGen']),
			// aes加密
			encryptText() {
				this.handleEncrypt(this.plain_text).then(() => {
					this.ciphertext = this.getCiphertext;
				}).catch(err => {
					this.$Message.error(err);
					console.error("Encryption failed: ", err);
				});
			},
			// aes解密
			decryptText() {
				this.handleDecrypt(this.ciphertext).then(() => {
					this.plain_text = this.getPlaintext;
				}).catch(err => {
					this.$Message.error(err);
					console.error("Dencryption failed: ", err)
				});
			},
			// 生成随机密码
			generatePassword() {
				this.handleRandomPassGen({ character: this.character, passLength: this.passLength }).then(() => {
					this.randomPass = this.getRandompass;
				}).catch((err) => {
					this.randomPass = ""
					this.$Message.error(err);
					console.error("Get random passowrd failed: ", err);
				})
			}
		}
	}
</script>

<style>
</style>