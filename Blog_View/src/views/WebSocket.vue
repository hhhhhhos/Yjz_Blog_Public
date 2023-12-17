<template>
  <div style="margin-top: 48px;">
    实时数据：{{ realTimeData }}
    <button @click="click">click</button>
    <button @click="click2">click2</button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      realTimeData: '', // 用于存储实时更新的数据
      websocket: null // WebSocket实例
    }
  },
  created () {
    this.setupWebSocket()
  },
  methods: {
    setupWebSocket () {
      this.websocket = new WebSocket('ws://localhost:8002/ws') // 创建WebSocket连接
      this.websocket.onopen = this.onWebSocketOpen // WebSocket连接打开时的处理函数
      this.websocket.onmessage = this.onWebSocketMessage // 收到WebSocket消息时的处理函数
      this.websocket.onclose = this.onWebSocketClose // WebSocket连接关闭时的处理函数
    },
    onWebSocketOpen () {
      console.log('链接成功')
    },
    onWebSocketMessage (event) {
      if (event.data) {
        this.realTimeData = event.data
      }
    },
    onWebSocketClose () {
      if (this.websocket) {
        this.websocket.close() // 关闭WebSocket连接
      }
    },
    sendMessag (message) {
      if (this.websocket && this.websocket.readyState === WebSocket.OPEN) {
        this.websocket.send(message)
        console.log('已发送') // 发送消息到WebSocket服务器
      } else {
        console.log('发送失败')
      }
    },
    click () {
      console.log(this.websocket.readyState)
    },
    click2 () {
      console.log('click')
      this.sendMessag('hello')
    }
  },
  beforeDestroy () {
    this.onWebSocketClose() // 在组件销毁前关闭WebSocket连接
  }
}
</script>
