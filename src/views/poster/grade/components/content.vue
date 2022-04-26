<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('poster.grade.welcome') }}
    </a-typography-title>
    <a-divider class="panel-border" />
    <a-table
      :columns="columns"
      :data="data"	
      :pagination="pagination"
      :filter-icon-align-left="true"
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
        <a-button type="outline" status="success" @click="onGrade(record)">{{ t('poster.grade') }}</a-button>
      </template>
    </a-table>
  </a-col>
  <a-image-preview
    v-model:visible="visible"
    :src="imgurl"
  />
</template>

<script lang="ts" setup>
import { ref, reactive, h } from 'vue'
import { IconSearch } from '@arco-design/web-vue/es/icon'
import { Modal } from '@arco-design/web-vue'
import { useI18n } from 'vue-i18n/index'
import { useGradeStore } from '@/store'

const { t } = useI18n()

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
    slotName: 'summary',
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
  {
    title: 'CST',
    major: 'CST',
    author: 'CST',
    summary: 'CST',
    url: 'CST',
  }
])

const visible = ref(false)
const imgurl = ref('')
const onShowImg = (url: string) => {
  imgurl.value = url
  visible.value = true
}
const emits = defineEmits(['onClick'])
const gradeStore = useGradeStore()
const onGrade = (record: any) => {
  emits('onClick', true)
  gradeStore.setRecord(record)
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
