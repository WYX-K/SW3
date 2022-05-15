<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('home.rules.welcome') }}
    </a-typography-title>
    <a-divider class="panel-border" />
    <a-form
      ref="formRef"
      size="large"
      auto-label-width
      :model="form"
      :style="{width:'600px'}"
      @submit="handleSubmit"
    >
      <a-form-item
        field="num_headjudge"
        :label="t('rules.num_headjudge.label')"
      >
        <a-input-number
          v-model="form.num_headjudge"
          mode="button"
          :min="2"
          :default-value="2"
        />
      </a-form-item>
      <a-form-item
        field="num_judges"
        :label="t('rules.num_judges.label')"
      >
        <a-input-number
          v-model="form.num_judges"
          mode="button"
          :min="14"
          :default-value="14"
        />
      </a-form-item>
      <a-form-item
        field="num_firstprize"
        :label="t('rules.num_firstprize.label')"
      >
        <a-input-number v-model="form.num_firstprize" mode="button" :min="1" />
      </a-form-item>
      <a-form-item
        field="num_secondprize"
        :label="t('rules.num_secondprize.label')"
      >
        <a-input-number v-model="form.num_secondprize" mode="button" :min="1" />
      </a-form-item>
      <a-form-item
        field="num_thirdprize"
        :label="t('rules.num_thirdprize.label')"
      >
        <a-input-number v-model="form.num_thirdprize" mode="button" :min="1" />
      </a-form-item>
      <a-form-item>
        <a-space>
          <a-button type="primary" html-type="submit">{{ t('poster.upload.submit') }}</a-button>
          <a-button @click="$refs.formRef.resetFields()">{{ t('poster.upload.reset') }}</a-button>
        </a-space>
      </a-form-item>
    </a-form>
  </a-col>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import { Message, Modal } from '@arco-design/web-vue'
import { useI18n } from 'vue-i18n/index'
import { postRules } from '@/api/rules'

const { t } = useI18n()
const formRef = ref()
const form = reactive({
  num_headjudge: 2,
  num_firstprize: 1,
  num_secondprize: 1,
  num_judges: 14,
  num_thirdprize: 1,
})
const changeConRules = async (form: any) => {
  const data = new FormData()
  data.append('num_headjudge', form.num_headjudge)
  data.append('num_firstprize', form.num_firstprize)
  data.append('num_judges', form.num_judges)
  data.append('num_secondprize', form.num_secondprize)
  data.append('num_thirdprize', form.num_thirdprize)
  const res = await postRules(data)
  if (res.status === 200) {
    Message.success(t('upload.success'))
    form.title = ''
    form.author = ''
    form.major = ''
    form.summary = ''
    form.fileList = []
    form.authorEmail = ''
  } else if (res.status === 205) {
    Message.warning(t('upload.fail'))
  }
}
const handleSubmit = (e: any) => {
  if (typeof (e.errors) === 'undefined') {
    Modal.confirm({
      title: t('rules.modal.title'),
      content: t('rules.modal.content'),
      okText: t('poster.modal.confirm'),
      cancelText: t('poster.modal.cancel'),
      onOk: () => {
        changeConRules(e.values)
      }
    })
  }
}
</script>

<style scoped lang="less">
  .banner {
    width: 100%;
    padding: 20px 20px 0 20px;
    background-color: var(--color-bg-2);
    border-radius: 4px 4px 0 0;
  }

</style>
