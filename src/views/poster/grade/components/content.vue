<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('poster.grade.welcome') }}
    </a-typography-title>
    <a-divider class="panel-border" />
    <a-spin :loading="loading" tip="This may take a while..." style="width: 100%">
      <a-table
        :columns="columns"
        :data="data.list"	
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
          <a-button type="outline" status="success" @click="onGrade(record)">{{ record.grade?t('poster.graded'):t('poster.grade') }}</a-button>
        </template>
      </a-table>
    </a-spin>
  </a-col>
  <a-image-preview
    v-model:visible="visible"
    :src="imgurl"
  />
</template>

<script lang="ts" setup>
import { ref, reactive, h, computed, onMounted, onActivated } from 'vue'
import { IconSearch } from '@arco-design/web-vue/es/icon'
import { Message, Modal } from '@arco-design/web-vue'
import { useI18n } from 'vue-i18n/index'
import consola from 'consola'
import { getPoster } from '@/api/poster'
import { useUserStore } from '@/store'
import { getGrade } from '@/api/grade'

const { t } = useI18n()

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

const visible = ref(false)
const imgurl = ref('')
const onShowImg = (url: string) => {
  imgurl.value = url
  visible.value = true
}

const emits = defineEmits(['onClick'])
const onGrade = (record: any) => {
  emits('onClick', true)
  sessionStorage.setItem('POSTER', JSON.stringify(record))
}

// 获取列表
const pagination = reactive({
  pageSize: 7,
  current: 1,
  total: 0,
  hideOnSinglePage: true
})
const loading = ref(false)
const userStore = useUserStore()
const getPosterList = async () => {
  const major = userStore.role === 'judge' ? sessionStorage.getItem('MAJOR') : 'DST'
  const params = {
    pageNum: pagination.current - 1,
    pageSize: pagination.pageSize,
    major,
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
    } else if (res.status === 201) {
      Message.error(t('poster.get.fail'))
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
const getGradeList = async () => {
  const params = {
    judgename: userStore.username,
    role: userStore.role,
  }
  try {
    const res = await getGrade({ params })
    if (res.status === 200) {
      data.list.map((item: any) => {
        if (res.data.includes(item.id.toString())) {
          item.grade = true
        } else {
          item.grade = false
        }
        return item
      })
    }
  } catch (e) {
    consola.error(e)
  }
}
let n = 0
onMounted(async () => {
  await getPosterList()
  getGradeList()
  n = 1
})
onActivated(() => {
  if (n === 1) {
    getGradeList()
  }
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
