<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('poster.upload.welcome') }}
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
        field="title"
        :label="t('upload.title.label')"
        :rules="[{required:true,message: t('upload.title.tip')}]"
        :validate-trigger="['change','input']"
      >
        <a-input v-model="form.title" :placeholder="t('upload.title.tip')" />
      </a-form-item>
      <a-form-item
        field="author"
        :label="t('upload.author.label')"
        :rules="[{required:true, message:t('upload.author.tip')}]"
        :validate-trigger="['change','input']"
      >
        <a-input v-model="form.author" :placeholder="t('upload.author.tip')" />
      </a-form-item>
      <a-form-item
        field="authorEmail"
        :label="t('upload.authorEmail.label')"
        :rules="[{required:true, message:t('upload.authorEmail.tip')}]"
        :validate-trigger="['change','input']"
      >
        <a-input v-model="form.authorEmail" :placeholder="t('upload.authorEmail.tip')">
          <template #append>
            @mail.uic.edu.cn
          </template>
        </a-input>
      </a-form-item>
      <a-form-item 
        field="major" 
        :label="t('upload.major.label')" 
        :rules="[{required:true, message:t('upload.major.tip')}]"
      >
        <a-select v-model="form.major" :placeholder="t('upload.major.tip')">
          <a-option value="CST">CST</a-option>
          <a-option value="DS">DS</a-option>
          <a-option value="FM">FM</a-option>
          <a-option value="STAT">STAT</a-option>
          <a-option value="APSY">APSY</a-option>
          <a-option value="ENVS">ENVS</a-option>
          <a-option value="FST">FST</a-option>
        </a-select>
      </a-form-item>
      <a-form-item 
        field="summary" 
        :label="t('upload.summary.label')" 
        :rules="[{required:true, message:t('upload.summary.tip')}]"
      >
        <a-textarea 
          v-model="form.summary" 
          :placeholder="t('upload.summary.tip')" 
          auto-size
          :allow-clear="true"
        />
      </a-form-item>
      <a-form-item 
        field="upload" 
        :rules="rules"
      >
        <a-upload
          v-model:file-list="form.fileList"
          :auto-upload="false"
          list-type="picture-card"
          action="/"
          :limit="1"
          accept="image/*"
          image-preview
        />
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
import { reactive } from 'vue'
import { Message, Modal } from '@arco-design/web-vue'
import { useI18n } from 'vue-i18n/index'
import { postPoster } from '@/api/poster'

const { t } = useI18n()
const form = reactive({
  title: '',
  author: '',
  authorEmail: '',
  major: '',
  summary: '',
  fileList: [],
})
const rules = [{
  validator: (value: any, cb: any) => {
    if (form.fileList.length === 0) {
      cb(t('upload.image.tip'))
    }
  },
  required: true
}]
const uploadPosterInfo = async (form: any) => {
  const data = new FormData()
  data.append('title', form.title)
  data.append('author', form.author)
  data.append('major', form.major)
  data.append('summary', form.summary)
  data.append('file', form.fileList[0].file)
  data.append('author_email', `${ form.authorEmail }@mail.uic.edu.cn`)
  const res = await postPoster(data)
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
      title: t('upload.modal.title'),
      content: t('upload.modal.content'),
      okText: t('poster.modal.confirm'),
      cancelText: t('poster.modal.cancel'),
      onOk: () => {
        uploadPosterInfo(e.values)
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
