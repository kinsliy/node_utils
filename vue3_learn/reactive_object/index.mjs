import { reactive } from "./base.mjs";

let data = { name: "Vue3", count: 0 };
let reactiveData = reactive(data);

// 测试响应式
reactiveData.name; // 控制台显示：获取 name
reactiveData.count = 1; // 控制台显示：设置 count: 1
