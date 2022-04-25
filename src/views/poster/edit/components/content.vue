<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('poster.edit.welcome') }}
    </a-typography-title>
    <a-divider class="panel-border" />
    <a-table
      v-model:selectedKeys="selectedKeys"
      :columns="columns"
      :data="data"	
      :pagination="pagination"
      :filter-icon-align-left="true"
      :row-selection="rowSelection"
      @page-change="handlePageChange"
    >
      <template #filter="{ filterValue, setFilterValue, handleFilterConfirm, handleFilterReset}">
        <div class="custom-filter">
          <a-space direction="vertical">
            <a-input :model-value="filterValue[0]" @input="(value: string)=>setFilterValue([value])" />
            <div class="custom-filter-footer">
              <a-button @click="handleFilterConfirm">{{ t('poster.filter.confirm') }}</a-button>
              <a-button @click="handleFilterReset">{{ t('poster.filter.reset') }}</a-button>
            </div>
          </a-space>
        </div>
      </template>
      <template #summary="{ record }">
        <a-button @click="Modal.info({ title:t('poster.table.summary'), content:record.summary })">{{ t('poster.imageBtn.title') }}</a-button>
      </template>
      <template #image="{ record }">
        <a-button @click="onShowImg(record.url)">{{ t('poster.imageBtn.title') }}</a-button>
      </template>
      <template #action="{ record }">
        <a-button type="outline" status="success" @click="onEdit(record)">{{ t('poster.editBtn.title') }}</a-button>
      </template>
    </a-table>
    <a-divider class="panel-border" />
    <a-button v-show="isBtnShow" style="position:absolute; right:5%" type="primary">{{ t('poster.delete') }}</a-button>
  </a-col>
  <a-image-preview
    v-model:visible="visible"
    :src="imgurl"
  />
  <a-modal
    v-model:visible="isShowModel"
    :title="t('edit.modal.title')"
    unmount-on-close
    :footer="false"
  >
    <a-form
      ref="formRef"
      size="middle"
      :model="form"
      :style="{width:'480px'}"
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
        :rules="[{required:true, message:t('upload.image.tip')}]"
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
  </a-modal>
</template>

<script lang="ts" setup>
import { ref, reactive, h, computed } from 'vue'
import { IconSearch } from '@arco-design/web-vue/es/icon'
import { Modal } from '@arco-design/web-vue'
import { useI18n } from 'vue-i18n/index'
import consola from 'consola'

const { t } = useI18n()

const selectedKeys = ref([])
const isBtnShow = computed(() => selectedKeys.value.length > 0)

const rowSelection = {
  type: 'checkbox',
  showCheckedAll: true
}

const columns = [
  {
    title: t('poster.table.title'),
    dataIndex: 'title',
    filterable: {
      filter: (value: string, record: { title: string | any[]; }) => record.title.includes(value),
      icon: () => h(IconSearch),
      slotName: 'filter',
    },
  },
  {
    title: t('poster.table.major'),
    dataIndex: 'major',
    filterable: {
      filters: [{
        text: 'CST',
        value: 'CST',
      }, {
        text: 'DS',
        value: 'DS',
      }, {
        text: 'STAT',
        value: 'STAT',
      }, {
        text: 'ENVS',
        value: 'ENVS',
      }, {
        text: 'FM',
        value: 'FM',
      }, {
        text: 'APSY',
        value: 'APSY',
      }],
      filter: (value:string, row: any) => row.major.includes(value),
      multiple: true,
    }
  },
  {
    title: t('poster.table.author'),
    dataIndex: 'author',
    filterable: {
      filter: (value: any, record: { author: string | any[]; }) => record.author.includes(value),
      icon: () => h(IconSearch),
      alignLeft: true,
      slotName: 'filter',
    },
  },
  {
    title: t('poster.table.summary'),
    dataIndex: 'summary',
  },
  {
    title: t('poster.table.image'),
    slotName: 'image',
  },
  {
    title: t('poster.table.action'),
    slotName: 'action',
    fixed: 'right',
  }
]
const data = reactive([
])

const visible = ref(false)
const imgurl = ref('')
const onShowImg = (url: string) => {
  imgurl.value = url
  visible.value = true
}

const isShowModel = ref(false)
const form = reactive({
  id: '',	
  title: '',
  author: '',
  major: '',
  summary: '',
  fileList: [],
})
const onEdit = (item: object) => {
  isShowModel.value = true
}
const uploadPosterInfo = async (form: any) => {
  consola.success(form)
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
        form.title = ''
        form.author = ''
        form.major = ''
        form.summary = ''
        form.fileList = []
      }
    })
  }
}
const pagination = reactive({
  pageSize: 10,
  current: 1,
  total: data.length,
  hideOnSinglePage: true
})
const handlePageChange = (page: number) => {
  console.log(page)
  pagination.current = page
}

</script>

<style scoped lang="less">
  .banner {
    width: 100%;
    padding: 20px 20px 0 20px;
    background-color: var(--color-bg-2);
    border-radius: 4px 4px 0 0;
  }

  .custom-filter {
  padding: 20px;
  background: var(--color-bg-5);
  border: 1px solid var(--color-neutral-3);
  border-radius: var(--border-radius-medium);
  box-shadow: 0 2px 5px rgb(0 0 0 / 10%);
}

.custom-filter-footer {
  display: flex;
  justify-content: space-between;
}
</style>
