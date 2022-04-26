import { defineStore } from 'pinia'
import { RecordProps } from './types'

const useUserStore = defineStore('grade', {
  state: () => ({
    record: {
      title: '',
      author: '',
      summary: '',
      url: '',
      major: '',
    },
  }),

  actions: {
    getRecord():RecordProps {
      return this.record
    },
      
    setRecord(record: RecordProps) {
      this.record = record
    }
  },
})

export default useUserStore
