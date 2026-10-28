window.config = {
  api: ["https://vercdn.beibeicloud.shop/bei","https://netcdn.beibeicloud.shop/bei","https://kcd.beibeicloud.shop/api/v1","https://cdn3.beibeicloud.shop/api/v1"],
  subscribe: "https://kcd.beibeicloud.shop",
  clients:[
      { id: 11, label: "Win一键客户端" },
      { id: 12, label: "Mac一键客户端" },
      { id: 13, label: "安卓一键客户端" },
      { id: 37, label: "IOS一键客户端" }
    ],
  // 主题配置
  defaultPath: "/",
  fontFamily: "'Roboto', sans-serif",
  miniDrawer: false,
  container: true,
  themeDirection: "ltr",
  title: "贝贝云",
  title_split: " - ",
  background_url: "",
  description: "快又稳",
  logo: "",
  languages: ["en-US","zh-CN","zh-TW"],
  emojiEndpoint: "https://cdn.jsdelivr.net/npm/emoji-datasource-apple/img/apple/64/{{code}}.png",
  startYear: 2024,
  crispWebsiteId: "17023143-8c98-4e8a-9df7-8760ba285c5d",
  // 紧急公告配置（纯前端读取，不依赖后端 API）
  emergencyNotice: {
    enabled: false, // 改为 true 后弹窗
    title: "紧急公告",
    content: "官网服务器异常离线，官网登录和客户端登录暂时不可用。\n我们正在紧急处理中，耐心等待恢复。预计最慢24小时内恢复。非常抱歉", // 支持使用 \n 换行
    confirmText: "我知道了"
  },
  // 图片上传配置
  imageUpload: {
    enabled: true,
    provider: "imgbb",
    imgbbApiKey: "e33b83bab9920dccd0defbf87e0bb28c" // 请替换为实际的ImgBB API key
  },
  // 官网配置
  officialWebsite: "888.beibei.cloud",
  website: "111.2beibei.com  333.2beibei.com 444.2beibei.com",
  // 主题颜色配置
  themeColors: {
    primary: {
      dark: ["#1c2134", "#1f294d", "#243462", "#273e83", "#2c4db0", "#305bdd", "#567fe9", "#80a4f4", "#a9c5f8", "#d2e2fb"],
      light: ["#E0F7F4", "#B3EBE3", "#86DFD2", "#59D3C1", "#45C4A9", "#3AB09A", "#2F9C8B", "#24887C", "#19746D", "#0E605E"]
    }
  }
};



