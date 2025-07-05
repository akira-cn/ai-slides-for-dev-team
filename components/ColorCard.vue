<!--
Component: ColorCard
Description: 彩色马卡龙风格的卡片组件，支持emoji图标和自定义颜色主题
Usage: <ColorCard emoji="🎯" title="标题" description="描述文字" color="blue" />
-->

<template>
  <div :class="cardClasses">
    <div v-if="emoji" class="text-2xl mb-2">{{ emoji }}</div>
    <div class="font-semibold" :class="titleClasses">{{ title }}</div>
    <div v-if="description" class="text-sm text-gray-600 dark:text-gray-300 mt-1">{{ description }}</div>
    <slot></slot>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  emoji: {
    type: String,
    default: ''
  },
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    default: ''
  },
  color: {
    type: String,
    default: 'blue',
    validator: (value) => [
      'blue', 'green', 'purple', 'red', 'orange', 
      'yellow', 'pink', 'teal', 'indigo', 'gray'
    ].includes(value)
  },
  size: {
    type: String,
    default: 'normal',
    validator: (value) => ['small', 'normal', 'large'].includes(value)
  },
  centered: {
    type: Boolean,
    default: false
  }
})

const cardClasses = computed(() => {
  const baseClasses = 'rounded-lg transition-all duration-200 hover:shadow-md'
  const sizeClasses = {
    small: 'p-3',
    normal: 'p-4',
    large: 'p-6'
  }
  const colorClasses = {
    blue: 'bg-blue-50 border border-blue-100',
    green: 'bg-green-50 border border-green-100',
    purple: 'bg-purple-50 border border-purple-100',
    red: 'bg-red-50 border border-red-100',
    orange: 'bg-orange-50 border border-orange-100',
    yellow: 'bg-yellow-50 border border-yellow-100',
    pink: 'bg-pink-50 border border-pink-100',
    teal: 'bg-teal-50 border border-teal-100',
    indigo: 'bg-indigo-50 border border-indigo-100',
    gray: 'bg-gray-50 border border-gray-100'
  }
  const alignClasses = props.centered ? 'text-center' : ''
  
  return `${baseClasses} ${sizeClasses[props.size]} ${colorClasses[props.color]} ${alignClasses}`
})

const titleClasses = computed(() => {
  const colorClasses = {
    blue: 'text-blue-700',
    green: 'text-green-700',
    purple: 'text-purple-700',
    red: 'text-red-700',
    orange: 'text-orange-700',
    yellow: 'text-yellow-700',
    pink: 'text-pink-700',
    teal: 'text-teal-700',
    indigo: 'text-indigo-700',
    gray: 'text-gray-700'
  }
  
  return colorClasses[props.color]
})
</script>

<style scoped>
/* 支持深色主题 */
.dark .bg-blue-50 {
  @apply bg-blue-900/20;
}
.dark .bg-green-50 {
  @apply bg-green-900/20;
}
.dark .bg-purple-50 {
  @apply bg-purple-900/20;
}
.dark .bg-red-50 {
  @apply bg-red-900/20;
}
.dark .bg-orange-50 {
  @apply bg-orange-900/20;
}
.dark .bg-yellow-50 {
  @apply bg-yellow-900/20;
}
.dark .bg-pink-50 {
  @apply bg-pink-900/20;
}
.dark .bg-teal-50 {
  @apply bg-teal-900/20;
}
.dark .bg-indigo-50 {
  @apply bg-indigo-900/20;
}
.dark .bg-gray-50 {
  @apply bg-gray-900/20;
}

.dark .text-blue-700 {
  @apply text-blue-300;
}
.dark .text-green-700 {
  @apply text-green-300;
}
.dark .text-purple-700 {
  @apply text-purple-300;
}
.dark .text-red-700 {
  @apply text-red-300;
}
.dark .text-orange-700 {
  @apply text-orange-300;
}
.dark .text-yellow-700 {
  @apply text-yellow-300;
}
.dark .text-pink-700 {
  @apply text-pink-300;
}
.dark .text-teal-700 {
  @apply text-teal-300;
}
.dark .text-indigo-700 {
  @apply text-indigo-300;
}
.dark .text-gray-700 {
  @apply text-gray-300;
}
</style>