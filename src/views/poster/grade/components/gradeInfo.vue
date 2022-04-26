<template>
  <a-col class="banner">
    <a-row justify="center" align="center">
      <a-col :span="8">
        <a-card hoverable :style="{ width: '300px', height: '580px' }">
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
                src="https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/a20012a2d4d5b9db43dfc6a01fe508c0.png~tplv-uwbnlip3yd-webp.webp"
              />
            </div>
          </template>
          <a-card-meta :title="data.record.title">
            <template #description>
              Card content <br />
              Card content
            </template>
          </a-card-meta>
        </a-card>
      </a-col>
      <a-col :span="12">
        <a-form
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
import { reactive, onActivated, computed } from 'vue'
import { useI18n } from 'vue-i18n/index'
import { useGradeStore } from '@/store'

const { t } = useI18n()

const emits = defineEmits(['onClick'])
const goBack = () => {
  emits('onClick', false)
}
const data = reactive({
  record: {
    title: '',
    author: '',
    summary: '',
    major: '',
    url: '',
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
  const gradeStore = useGradeStore()
  console.log(gradeStore.getRecord())
  data.record = gradeStore.getRecord()
})

const handleSubmit = () => {
  console.log(formdata.value)
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