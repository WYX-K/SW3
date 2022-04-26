<template>
  <a-col class="banner">
    <a-row justify="center">
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
        <a-row>
          <a-form :model="form" :style="{width:'600px'}" @submit="handleSubmit">
            <a-form-item field="visual_layout" :label="t('poster.grade.visual_layout')">
              <a-slider 
                v-model:model-value="form.visual_layout"	
                :default-value="0" 
                :style="{ width: '300px' }"
                :step="0.1"
                :max="5"
                show-input
              />
            </a-form-item>
            <a-form-item field="poster_organization" :label="t('poster.grade.poster_organization')">
              <a-slider 
                v-model:model-value="form.poster_organization"	
                :default-value="0" 
                :style="{ width: '300px' }"
                :step="0.1"
                :max="5"
              />
            </a-form-item>
            <a-form-item field="poster_content" :label="t('poster.grade.poster_content')">
              <a-slider 
                v-model:model-value="form.poster_content"	
                :default-value="0" 
                :style="{ width: '300px' }"
                :step="0.1"
                :max="5"
              />
            </a-form-item>
            <a-form-item field="written_language" :label="t('poster.grade.written_language')">
              <a-slider 
                v-model:model-value="form.written_language"	
                :default-value="0" 
                :style="{ width: '300px' }"
                :step="0.1"
                :max="5"
              />
            </a-form-item>
            <a-form-item field="oral_presentation" :label="t('poster.grade.oral_presentation')">
              <a-slider 
                v-model:model-value="form.oral_presentation"	
                :default-value="0" 
                :style="{ width: '300px' }"
                :step="0.1"
                :max="5"
              />
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
        </a-row>
      </a-col>
    </a-row>
  </a-col>
</template>

<script setup lang="ts">
import { reactive, onActivated } from 'vue'
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
onActivated(() => {
  const gradeStore = useGradeStore()
  console.log(gradeStore.getRecord())
  data.record = gradeStore.getRecord()
})

const form = reactive({
  visual_layout: 0,
  poster_organization: 0,
  poster_content: 0,
  written_language: 0,
  oral_presentation: 0,
})
const handleSubmit = () => {
  
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