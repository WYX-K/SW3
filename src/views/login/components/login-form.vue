<template>
  <a-switch
    v-model="localeValue" 
    class="switch" 
    checked-color="#F53F3F"
    unchecked-color="#14C9C9"
    size="large"
    checked-value="en-US"
    unchecked-value="zh-CN"
    @change="switchChange"
  >
    <template #checked>
      EN
    </template>
    <template #unchecked>
      中
    </template>
  </a-switch>
  <div class="login-form-wrapper">
    <div class="login-form-title">{{ t('login.form.title') }}</div>
    <div class="login-form-sub-title">{{ t('login.form.title') }}</div>
    <div class="login-form-error-msg">{{ errorMessage }}</div>
    <a-form
      ref="loginForm"
      :model="userInfo"
      class="login-form"
      layout="vertical"
      auto-label-width
      @submit="handleSubmit"
    >
      <a-form-item
        field="username"
        :rules="[{ required: true, message: t('login.form.userName.errMsg') }]"
        :validate-trigger="['change', 'blur']"
        hide-label
      >
        <a-input
          v-model="userInfo.username"
          :placeholder="t('login.form.userName.placeholder')"
        >
          <template #prefix>
            <icon-user />
          </template>
        </a-input>
      </a-form-item>
      <a-form-item
        field="password"
        :rules="[{ required: true, message: t('login.form.password.errMsg') }]"
        :validate-trigger="['change', 'blur']"
        hide-label
      >
        <a-input-password
          v-model="userInfo.password"
          :placeholder="t('login.form.password.placeholder')"
          allow-clear
          autocomplete="off"
        >
          <template #prefix>
            <icon-lock />
          </template>
        </a-input-password>
      </a-form-item>
      <a-space :size="16" direction="vertical">
        <a-button
          type="primary"
          html-type="submit"
          long
          :loading="loading"
        >
          {{ t('login.form.login') }}
        </a-button>
      </a-space>
    </a-form>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ValidatedError } from '@arco-design/web-vue/es/form/interface'
import { useI18n } from 'vue-i18n/index'
import useLoading from '@/hooks/loading'
import { LoginData } from '@/api/login'
import useLocale from '@/hooks/locale'
import useUser from '@/hooks/user'

const router = useRouter()
const { t } = useI18n()
const errorMessage = ref('')
const { loading, setLoading } = useLoading()
const userInfo = reactive({
  username: 'simon',
  password: 'simon',
})

const handleSubmit = async ({
  errors,
  values,
}: {
    errors: Record<string, ValidatedError> | undefined
    values: LoginData
  }) => {
  if (!errors) {
    const data = new FormData()
    data.append('username', values.username)
    data.append('pwd', values.password)
    const { login } = useUser()
    setLoading(true)
    await login(data, router, t)
    setLoading(false)
  }
}
const setRememberPassword = () => {
  //
}

const localeValue = ref('')
const locale = useLocale()
if (locale.currentLocale.value === 'zh-CN') {
  localeValue.value = 'zh-CN'
} else {
  localeValue.value = 'en-US'
}
const switchChange = (value: string) => {
  locale.changeLocale(value)
}
</script>

<style lang="less" scoped>
  .switch{
    position: absolute;
    right: 5vh;
    top: 2vh;
  }
  .login-form {
    &-wrapper {
      width: 320px;
    }

    &-title {
      color: var(--color-text-1);
      font-weight: 500;
      font-size: 24px;
      line-height: 32px;
    }

    &-sub-title {
      color: var(--color-text-3);
      font-size: 16px;
      line-height: 24px;
    }

    &-error-msg {
      height: 32px;
      color: rgb(var(--red-6));
      line-height: 32px;
    }

    &-password-actions {
      display: flex;
      justify-content: space-between;
    }

    &-register-btn {
      color: var(--color-text-3) !important;
    }
  }
</style>
