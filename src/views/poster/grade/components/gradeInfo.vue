<template>
  <a-col class="banner">
    <a-row justify="center" align="center">
      <a-col :span="8">
        <a-card hoverable :style="{ width: '300px', height: '550px' }">
          <template #cover>
            <div
              :style="{
                height: '400px',
                overflow: 'hidden',
              }"
            >
              <a-image
                width="100%"
                height="100%"	
                alt="poster"
                :src="post.record.url"
              />
            </div>
          </template>
          <a-card-meta :title="post.record.title">
            <template #description>
              {{ post.record.author }}
              {{ post.record.major }}<br>
              {{ post.record.summary }}
            </template>
          </a-card-meta>
        </a-card>
      </a-col>
      <a-col :span="12">
        <a-form
          ref="formRef"
          :model="formdata"
          auto-label-width
          @submit="handleSubmit"
        >
          <a-form-item
            v-for="silder, index in silderdata"
            :key="index"
            :field="silder.field"
            :label="silder.label"
          >
            <a-slider 
              v-model:model-value="silder.data"	
              :default-value="0" 
              :style="{ width: '250px' }"
              :step="0.1"
              :max="5"
            />
            <a-tag color="arcoblue" style="margin-left:15px">{{ silder.data }}</a-tag>
          </a-form-item>
          <a-form-item>
            <a-space :size="180">
              <a-button type="primary" html-type="submit" style="width:300%">
                {{ t('poster.grade.submit') }}
              </a-button>
              <a-button type="outline" @click="goBack">
                {{ t('poster.grade.goback') }}
              </a-button>
            </a-space>
          </a-form-item>
        </a-form>
      </a-col>
    </a-row>
  </a-col>
</template>

<script setup lang="ts">
import { reactive, onActivated, computed, ref } from 'vue'
import { useI18n } from 'vue-i18n/index'
import consola from 'consola'
import { Message } from '@arco-design/web-vue'
import { useUserStore } from '@/store'
import { postGrade } from '@/api/grade'

const { t } = useI18n()
const formRef = ref()
const emits = defineEmits(['onClick'])
const goBack = () => {
  for (const silder of silderdata) {
    silder.data = 0
  }
  emits('onClick', false)
}
const post = reactive({
  record: {
    title: '',
    author: '',
    summary: '',
    major: '',
    url: '',
    id: '',
  },
})

const silderdata = reactive([
  {
    field: 'visual_layout',
    label: t('poster.grade.visual_layout'),
    data: 0,
  },
  {
    field: 'poster_organization',
    label: t('poster.grade.poster_organization'),
    data: 0,
  },
  {
    field: 'poster_content',
    label: t('poster.grade.poster_content'),
    data: 0,
  },
  {
    field: 'written_language',
    label: t('poster.grade.written_language'),
    data: 0,
  },
  {
    field: 'oral_presentation',
    label: t('poster.grade.oral_presentation'),
    data: 0,
  },
])
const formdata = computed(() => ({
  visual_layout: silderdata[0].data,
  poster_organization: silderdata[1].data,
  poster_content: silderdata[2].data,
  written_language: silderdata[3].data,
  oral_presentation: silderdata[4].data,
}))
onActivated(() => {
  post.record = JSON.parse(sessionStorage.getItem('POSTER') as string)
})

const userStore = useUserStore()
const handleSubmit = async () => {
  const data = new FormData()
  data.append('visual_layout', formdata.value.visual_layout.toString())
  data.append('poster_organization', formdata.value.poster_organization.toString())
  data.append('poster_content', formdata.value.poster_content.toString())
  data.append('written_language', formdata.value.written_language.toString())
  data.append('oral_presentation', formdata.value.oral_presentation.toString())
  data.append('id', post.record.id)
  data.append('role', userStore.role)
  data.append('judgename', sessionStorage.getItem('USERNAME') as string)
  try {
    const res = await postGrade(data)
    if (res.status === 200) {
      Message.success(t('poster.grade.success'))
    }
  } catch (e) {
    consola.error(e)
  }
}

</script>

<style lang="less" scoped>
    .banner {
    width: 100%;
    padding: 20px 20px 0 20px;
    background-color: var(--color-bg-2);
    border-radius: 4px 4px 0 0;
  }
</style>