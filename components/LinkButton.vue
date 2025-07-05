<!--
Component: LinkButton
Description: 链接按钮组件，支持多种样式和颜色主题
Usage: <LinkButton href="https://example.com" color="blue" variant="primary">点击访问</LinkButton>
-->

<template>
  <a 
    :href="href" 
    :target="target" 
    :class="buttonClasses"
    @click="handleClick"
  >
    <span v-if="icon" class="mr-2">{{ icon }}</span>
    <slot></slot>
    <span v-if="external && target === '_blank'" class="ml-1">↗</span>
  </a>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  href: {
    type: String,
    required: true
  },
  color: {
    type: String,
    default: 'blue',
    validator: (value) => [
      'blue', 'green', 'purple', 'red', 'orange', 
      'yellow', 'pink', 'teal', 'indigo', 'gray'
    ].includes(value)
  },
  variant: {
    type: String,
    default: 'primary',
    validator: (value) => ['primary', 'secondary', 'outline', 'ghost'].includes(value)
  },
  size: {
    type: String,
    default: 'normal',
    validator: (value) => ['small', 'normal', 'large'].includes(value)
  },
  icon: {
    type: String,
    default: ''
  },
  external: {
    type: Boolean,
    default: false
  },
  target: {
    type: String,
    default: '_self'
  },
  disabled: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['click'])

const buttonClasses = computed(() => {
  const baseClasses = 'inline-flex items-center justify-center font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2'
  
  const sizeClasses = {
    small: 'px-3 py-1.5 text-sm',
    normal: 'px-4 py-2 text-base',
    large: 'px-6 py-3 text-lg'
  }
  
  const variantClasses = {
    primary: {
      blue: 'bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500',
      green: 'bg-green-600 text-white hover:bg-green-700 focus:ring-green-500',
      purple: 'bg-purple-600 text-white hover:bg-purple-700 focus:ring-purple-500',
      red: 'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500',
      orange: 'bg-orange-600 text-white hover:bg-orange-700 focus:ring-orange-500',
      yellow: 'bg-yellow-600 text-white hover:bg-yellow-700 focus:ring-yellow-500',
      pink: 'bg-pink-600 text-white hover:bg-pink-700 focus:ring-pink-500',
      teal: 'bg-teal-600 text-white hover:bg-teal-700 focus:ring-teal-500',
      indigo: 'bg-indigo-600 text-white hover:bg-indigo-700 focus:ring-indigo-500',
      gray: 'bg-gray-600 text-white hover:bg-gray-700 focus:ring-gray-500'
    },
    secondary: {
      blue: 'bg-blue-100 text-blue-700 hover:bg-blue-200 focus:ring-blue-500',
      green: 'bg-green-100 text-green-700 hover:bg-green-200 focus:ring-green-500',
      purple: 'bg-purple-100 text-purple-700 hover:bg-purple-200 focus:ring-purple-500',
      red: 'bg-red-100 text-red-700 hover:bg-red-200 focus:ring-red-500',
      orange: 'bg-orange-100 text-orange-700 hover:bg-orange-200 focus:ring-orange-500',
      yellow: 'bg-yellow-100 text-yellow-700 hover:bg-yellow-200 focus:ring-yellow-500',
      pink: 'bg-pink-100 text-pink-700 hover:bg-pink-200 focus:ring-pink-500',
      teal: 'bg-teal-100 text-teal-700 hover:bg-teal-200 focus:ring-teal-500',
      indigo: 'bg-indigo-100 text-indigo-700 hover:bg-indigo-200 focus:ring-indigo-500',
      gray: 'bg-gray-100 text-gray-700 hover:bg-gray-200 focus:ring-gray-500'
    },
    outline: {
      blue: 'border-2 border-blue-600 text-blue-600 hover:bg-blue-50 focus:ring-blue-500',
      green: 'border-2 border-green-600 text-green-600 hover:bg-green-50 focus:ring-green-500',
      purple: 'border-2 border-purple-600 text-purple-600 hover:bg-purple-50 focus:ring-purple-500',
      red: 'border-2 border-red-600 text-red-600 hover:bg-red-50 focus:ring-red-500',
      orange: 'border-2 border-orange-600 text-orange-600 hover:bg-orange-50 focus:ring-orange-500',
      yellow: 'border-2 border-yellow-600 text-yellow-600 hover:bg-yellow-50 focus:ring-yellow-500',
      pink: 'border-2 border-pink-600 text-pink-600 hover:bg-pink-50 focus:ring-pink-500',
      teal: 'border-2 border-teal-600 text-teal-600 hover:bg-teal-50 focus:ring-teal-500',
      indigo: 'border-2 border-indigo-600 text-indigo-600 hover:bg-indigo-50 focus:ring-indigo-500',
      gray: 'border-2 border-gray-600 text-gray-600 hover:bg-gray-50 focus:ring-gray-500'
    },
    ghost: {
      blue: 'text-blue-600 hover:bg-blue-50 focus:ring-blue-500',
      green: 'text-green-600 hover:bg-green-50 focus:ring-green-500',
      purple: 'text-purple-600 hover:bg-purple-50 focus:ring-purple-500',
      red: 'text-red-600 hover:bg-red-50 focus:ring-red-500',
      orange: 'text-orange-600 hover:bg-orange-50 focus:ring-orange-500',
      yellow: 'text-yellow-600 hover:bg-yellow-50 focus:ring-yellow-500',
      pink: 'text-pink-600 hover:bg-pink-50 focus:ring-pink-500',
      teal: 'text-teal-600 hover:bg-teal-50 focus:ring-teal-500',
      indigo: 'text-indigo-600 hover:bg-indigo-50 focus:ring-indigo-500',
      gray: 'text-gray-600 hover:bg-gray-50 focus:ring-gray-500'
    }
  }
  
  const disabledClasses = 'opacity-50 cursor-not-allowed pointer-events-none'
  
  return [
    baseClasses,
    sizeClasses[props.size],
    variantClasses[props.variant][props.color],
    props.disabled ? disabledClasses : ''
  ].join(' ')
})

const handleClick = (event) => {
  if (props.disabled) {
    event.preventDefault()
    return
  }
  emit('click', event)
}
</script>

<style scoped>
/* 深色主题支持 */
.dark .bg-blue-100 {
  @apply bg-blue-900/30;
}
.dark .bg-green-100 {
  @apply bg-green-900/30;
}
.dark .bg-purple-100 {
  @apply bg-purple-900/30;
}
.dark .bg-red-100 {
  @apply bg-red-900/30;
}
.dark .bg-orange-100 {
  @apply bg-orange-900/30;
}
.dark .bg-yellow-100 {
  @apply bg-yellow-900/30;
}
.dark .bg-pink-100 {
  @apply bg-pink-900/30;
}
.dark .bg-teal-100 {
  @apply bg-teal-900/30;
}
.dark .bg-indigo-100 {
  @apply bg-indigo-900/30;
}
.dark .bg-gray-100 {
  @apply bg-gray-900/30;
}

.dark .hover\:bg-blue-50:hover {
  @apply bg-blue-900/20;
}
.dark .hover\:bg-green-50:hover {
  @apply bg-green-900/20;
}
.dark .hover\:bg-purple-50:hover {
  @apply bg-purple-900/20;
}
.dark .hover\:bg-red-50:hover {
  @apply bg-red-900/20;
}
.dark .hover\:bg-orange-50:hover {
  @apply bg-orange-900/20;
}
.dark .hover\:bg-yellow-50:hover {
  @apply bg-yellow-900/20;
}
.dark .hover\:bg-pink-50:hover {
  @apply bg-pink-900/20;
}
.dark .hover\:bg-teal-50:hover {
  @apply bg-teal-900/20;
}
.dark .hover\:bg-indigo-50:hover {
  @apply bg-indigo-900/20;
}
.dark .hover\:bg-gray-50:hover {
  @apply bg-gray-900/20;
}
</style>