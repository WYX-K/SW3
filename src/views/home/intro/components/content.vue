<template>
  <a-col class="banner">
    <a-typography-title :heading="5" style="margin-top: 0">
      {{ t('home.welcome') }} {{ userInfo.name }}
    </a-typography-title>
    <a-divider class="panel-border" />
    <a-spin :loading="loading" tip="This may take a while..." style="width: 100%">
      <a-row justify="space-around">
        <a-col :span="8">
          <a-carousel
            indicator-type="slider"
            show-arrow="hover"
            auto-play
            style="width: 100%; height: 360px; border-radius: 4px; overflow: hidden"
          >
            <a-carousel-item v-for="(src, idx) in imageSrc.list" :key="idx">
              <div>
                <img :src="src" style="width: 100%" />
              </div>
            </a-carousel-item>
          </a-carousel>
        </a-col>
        <a-col :span="14">
          <div ref="chart" class="barchartContainer">
          </div>
        </a-col>
      </a-row>
    </a-spin>
  </a-col>
</template>

<script lang="ts" setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { useI18n } from 'vue-i18n/index'
import * as echarts from 'echarts'
import { useUserStore } from '@/store'
import { getPostersVote } from '@/api/vote'

const { t } = useI18n()
const chart = ref(null)
let myEcharts = reactive({})
const option = reactive({
  tooltip: {
    show: true
  },
  color: ['#2b4b6b'],
  title: {
    text: 'The top five most popular authors',
    subtext: new Date().toLocaleString(),
    textAlign: 'right',
    left: '80%',
  },
  xAxis: {
    type: 'category',
    data: [],
  }, // X轴
  yAxis: { 
    type: 'category',
    data: []
  }, // Y轴
  series: [
    {
      data: [],
      type: 'bar'
    }],
})
const init = () => {
  myEcharts = echarts.init(chart.value as unknown as HTMLElement)
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  myEcharts.setOption(option)
  window.onresize = () => {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    myEcharts.resize()
  }
}

const userStore = useUserStore()
const userInfo = computed(() => ({
  name: userStore.name,
}))
const imageSrc = reactive({
  list: []
})
const loading = ref(false)
onMounted(async () => {
  loading.value = true
  try {
    const res = await getPostersVote()
    const data = res.data
    for (const item of data) {
      if (item.url) {
        const url = `data:image/png;base64,${ item.url }`
        imageSrc.list.push(url as never)
      }
    }
    option.xAxis.data = data.map((item: { author: any }) => item.author)
    const max = data[0].vote + 2
    option.yAxis.data = [...Array(max).keys()] as never[]
    option.series[0].data = data.map((item: { vote: any }) => item.vote)
    init()
    
    loading.value = false
  } catch (e) {
    console.log(e)
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
  .barchartContainer {
    width: 100%;
    height: 360px;
  }
</style>
