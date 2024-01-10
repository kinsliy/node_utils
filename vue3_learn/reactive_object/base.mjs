export function reactive(obj) {
  return new Proxy(obj, {
    get(target, key) {
      console.log(`获取 ${key}`);
      return Reflect.get(target, key);
    },
    set(target, key, value) {
      console.log(`设置 ${key}: ${value}`);
      Reflect.set(target, key, value);
      // 这里可以触发更新逻辑
      return true;
    },
  });
}

