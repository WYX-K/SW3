<template>
  <a-col class="banner">
    <a-table
      :columns="columns"
      :data="data"
      :pagination="pagination"
      @page-change="handlePageChange"
    >
      <template #name-filter="{ filterValue, setFilterValue, handleFilterConfirm, handleFilterReset}">
        <div class="custom-filter">
          <a-space direction="vertical">
            <a-input :model-value="filterValue[0]" @input="(value:string)=>setFilterValue([value])" />
            <div class="custom-filter-footer">
              <a-button @click="handleFilterConfirm">{{ t('poster.filter.confirm') }}</a-button>
              <a-button @click="handleFilterReset">{{ t('poster.filter.cancel') }}</a-button>
            </div>
          </a-space>
        </div>
      </template>
      <template #image="{ record }">
        <a-button @click="onShowImg(record.id)">{{ t('poster.imageBtn.title') }}</a-button>
      </template>
      <template #action="{ record }">
        <a-button type="outline" status="success" @click="onVote(record.url)">{{ t('poster.actionBtn.title') }}</a-button>
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

const { t } = useI18n()

const columns = [
  {
    title: 'Name',
    dataIndex: 'name',
    filterable: {
      filter: (value: any, record: { name: string | any[]; }) => record.name.includes(value),
      slotName: 'name-filter',
      icon: () => h(IconSearch),
      alignLeft: true
    }
  },
  {
    title: 'Salary',
    dataIndex: 'salary',
    sortable: {
      sortDirections: ['ascend']
    },
  },
  {
    title: 'Address',
    dataIndex: 'address',
  },
  {
    title: 'Email',
    dataIndex: 'email',
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
const data = reactive([{
  key: '1',
  name: 'Jane Doe',
  salary: 23000,
  address: '32 Park Road, London',
  email: 'jane.doe@example.com'
},
{
  key: '2',
  name: 'Alisa Ross',
  salary: 25000,
  address: '35 Park Road, London',
  email: 'alisa.ross@example.com'
},
{
  key: '3',
  name: 'Kevin Sandra',
  salary: 22000,
  address: '31 Park Road, London',
  email: 'kevin.sandra@example.com'
},
{
  key: '4',
  name: 'Ed Hellen',
  salary: 17000,
  address: '42 Park Road, London',
  email: 'ed.hellen@example.com'
},
{
  key: '5',
  name: 'William Smith',
  salary: 27000,
  address: '62 Park Road, London',
  email: 'william.smith@example.com'
},
{
  key: '1',
  name: 'Jane Doe',
  salary: 23000,
  address: '32 Park Road, London',
  email: 'jane.doe@example.com'
},
{
  key: '2',
  name: 'Alisa Ross',
  salary: 25000,
  address: '35 Park Road, London',
  email: 'alisa.ross@example.com'
},
{
  key: '3',
  name: 'Kevin Sandra',
  salary: 22000,
  address: '31 Park Road, London',
  email: 'kevin.sandra@example.com'
},
{
  key: '4',
  name: 'Ed Hellen',
  salary: 17000,
  address: '42 Park Road, London',
  email: 'ed.hellen@example.com'
},
{
  key: '5',
  name: 'William Smith',
  salary: 27000,
  address: '62 Park Road, London',
  email: 'william.smith@example.com'
},
{
  key: '1',
  name: 'Jane Doe',
  salary: 23000,
  address: '32 Park Road, London',
  email: 'jane.doe@example.com'
},
{
  key: '2',
  name: 'Alisa Ross',
  salary: 25000,
  address: '35 Park Road, London',
  email: 'alisa.ross@example.com'
},
{
  key: '3',
  name: 'Kevin Sandra',
  salary: 22000,
  address: '31 Park Road, London',
  email: 'kevin.sandra@example.com'
},
{
  key: '4',
  name: 'Ed Hellen',
  salary: 17000,
  address: '42 Park Road, London',
  email: 'ed.hellen@example.com'
},
{
  key: '5',
  name: 'William Smith',
  salary: 27000,
  address: '62 Park Road, London',
  email: 'william.smith@example.com'
},
])

const visible = ref(false)
const imgurl = ref('')
const onShowImg = (url: string) => {
  imgurl.value = url
  visible.value = true
}
const onVote = (id: number) => {
  Modal.confirm({
    title: t('poster.sureVote.title'),
    content: t('poster.sureVote.content'),
    okText: t('poster.sureVote.okText'),
    cancelText: t('poster.sureVote.cancelText'),
    onOk: () => {
      console.log(id)
    },
    onCancel: () => {
      console.log('cancel')
    }
  })
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
