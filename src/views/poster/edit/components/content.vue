<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('poster.edit.welcome') }}
    </a-typography-title>
    <a-divider class="panel-border" />
    <a-spin :loading="loading" tip="This may take a while..." style="width: 100%">
      <a-table 
        :row-selection="rowSelection"
        :columns="columns"
        :data="data.list"	
        :pagination="pagination"
        :filter-icon-align-left="true"
        style="width: 100%"
        @page-change="handlePageChange"
        @select="onRowSelect"
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
          <a-button type="outline" status="success" @click="onEdit(record.id)">{{ t('poster.editBtn.title') }}</a-button>
        </template>
      </a-table>
    </a-spin>
    <a-divider class="panel-border" />
    <a-button
      v-show="isBtnShow"
      style="position:absolute; right:5%"
      type="primary"
      @click="onDeletePoster"
    >
      {{ t('poster.delete') }}
    </a-button>
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
      auto-label-width
      :model="form"
      :style="{width:'480px'}"
      @submit="handleSubmit"
    >
      <a-form-item
        field="title"
        :label="t('upload.title.label')"
        :validate-trigger="['change','input']"
      >
        <a-input v-model="form.title" :placeholder="t('upload.title.tip')" />
      </a-form-item>
      <a-form-item
        field="author"
        :label="t('upload.author.label')"
        :validate-trigger="['change','input']"
      >
        <a-input v-model="form.author" :placeholder="t('upload.author.tip')" />
      </a-form-item>
      <a-form-item
        field="authorEmail"
        :label="t('upload.authorEmail.label')"
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
import { ref, reactive, h, computed, onMounted } from 'vue'
import { IconSearch } from '@arco-design/web-vue/es/icon'
import { Message, Modal } from '@arco-design/web-vue'
import { useI18n } from 'vue-i18n/index'
import qs from 'qs'
import consola from 'consola'
import { getPoster, deletePoster, editPoster } from '@/api/poster'

const { t } = useI18n()
const formRef = ref()
const columns = [
  {
    title: computed(() => t('poster.table.title')),
    dataIndex: 'title',
    filterable: {
      filter: (value: string, record: { title: string | any[]; }) => record.title.includes(value),
      icon: () => h(IconSearch),
      slotName: 'filter',
    },
  },
  {
    title: computed(() => t('poster.table.major')),
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
      }, {
        text: 'FST',
        value: 'FST',
      }],
      filter: (value:string, row: any) => row.major.includes(value),
      multiple: true,
    }
  },
  {
    title: computed(() => t('poster.table.author')),
    dataIndex: 'author',
    filterable: {
      filter: (value: any, record: { author: string | any[]; }) => record.author.includes(value),
      icon: () => h(IconSearch),
      alignLeft: true,
      slotName: 'filter',
    },
  },
  {
    title: computed(() => t('poster.table.summary')),
    slotName: 'summary',
  },
  {
    title: computed(() => t('poster.table.image')),
    slotName: 'image',
  },
  {
    title: computed(() => t('poster.table.action')),
    slotName: 'action',
    fixed: 'right',
  }
]
const data = reactive({
  list: [],
})
const rowSelection = {
  type: 'checkbox',
}

// 删除海报
const selectedKeys = ref([])
const onRowSelect = (rowKeys: never[]) => {
  selectedKeys.value = rowKeys
}
const onDeletePoster = async () => {
  const data = qs.stringify({
    ids: selectedKeys.value,
  }, { arrayFormat: 'brackets' })
  try {
    const res = await deletePoster({ data })
    if (res.status === 200) {
      await getPosterList()
      Message.success(t('poster.delete.success'))
    }
  } catch (e) {
    consola.error(e)
  }
}
const isBtnShow = computed(() => selectedKeys.value.length > 0)

// 展示海报
const visible = ref(false)
const imgurl = ref('')
const onShowImg = (url: string) => {
  imgurl.value = url
  visible.value = true
}

// 修改海报
const isShowModel = ref(false)
const form = reactive({
  id: '',	
  title: '',
  author: '',    
  major: '',
  summary: '',
  authorEmail: '',
  fileList: [],
})
const changeItemID = ref(0)
const onEdit = (item: number) => {
  changeItemID.value = item
  isShowModel.value = true
}
const changePosterInfo = async (form: any) => {
  let authorEmail = `${ form.authorEmail }@mail.uic.edu.cn`
  let file = ''
  if (!form.authorEmail) {
    authorEmail = ''
  }
  if (form.fileList.length > 0) {
    file = form.fileList[0].file
  }
  const data = new FormData()
  data.append('title', form.title)
  data.append('author', form.author)
  data.append('major', form.major)
  data.append('summary', form.summary)
  data.append('file', file)
  data.append('author_email', authorEmail)
  data.append('id', changeItemID.value.toString())
  try {
    const res = await editPoster(data)
    if (res.status === 200) {
      Message.success(t('poster.edit.success'))
      isShowModel.value = false
      getPosterList()
      formRef.value.resetFields()
    }
  } catch (e) {
    consola.error(e)
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
        changePosterInfo(e.values)
      }
    })
  }
}

// 获取列表
const pagination = reactive({
  pageSize: 6,
  current: 1,
  total: data.list.length,
  hideOnSinglePage: true
})
const loading = ref(false)
const getPosterList = async () => {
  const params = {
    pageNum: pagination.current - 1,
    pageSize: pagination.pageSize,
    major: 'all',
  }
  try {
    loading.value = true
    const res = await getPoster({ params })
    if (res.status === 200) { 
      data.list = res.data.map((item: any) => {
        item.url = `data:image/png;base64,${ item.url }`
        item.key = item.id
        return item
      })
      pagination.total = res.data[0].total
      Message.success(t('poster.get.success'))
    }
  } catch (e) {
    consola.error(e)
  }
  loading.value = false
}
const handlePageChange = (page: number) => {
  pagination.current = page
  getPosterList()
}
onMounted(() => {
  getPosterList()
})
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
