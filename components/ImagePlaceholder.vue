<!--
Component: ImagePlaceholder
Description: 图片占位组件，默认300px宽高，支持自定义尺寸和占位内容
Usage: <ImagePlaceholder src="/path/to/image.jpg" alt="图片描述" />
-->

<template>
  <div :class="containerClasses" :style="containerStyle">
    <img 
      v-if="src && !imageError" 
      :src="src" 
      :alt="alt" 
      :class="imageClasses"
      @load="handleImageLoad"
      @error="handleImageError"
    />
    <div v-else :class="placeholderClasses">
      <div class="flex flex-col items-center justify-center h-full">
        <div class="text-4xl mb-2 opacity-50">{{ placeholderIcon }}</div>
        <div class="text-sm text-gray-500 text-center px-4">
          {{ placeholderText }}
        </div>
        <div v-if="showUploadHint" class="text-xs text-gray-400 mt-2">
          点击上传图片
        </div>
      </div>
    </div>
    <input 
      v-if="editable" 
      ref="fileInput"
      type="file"
      accept="image/*"
      class="hidden"
      @change="handleFileChange"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted, getCurrentInstance } from 'vue'

const props = defineProps({
  src: {
    type: String,
    default: ''
  },
  alt: {
    type: String,
    default: '图片'
  },
  width: {
    type: [String, Number],
    default: 300
  },
  height: {
    type: [String, Number],
    default: 300
  },
  rounded: {
    type: String,
    default: 'lg',
    validator: (value) => ['none', 'sm', 'md', 'lg', 'xl', 'full'].includes(value)
  },
  objectFit: {
    type: String,
    default: 'cover',
    validator: (value) => ['cover', 'contain', 'fill', 'none', 'scale-down'].includes(value)
  },
  placeholderIcon: {
    type: String,
    default: '🖼️'
  },
  placeholderText: {
    type: String,
    default: '图片占位符'
  },
  editable: {
    type: Boolean,
    default: false
  },
  showUploadHint: {
    type: Boolean,
    default: false
  },
  backgroundColor: {
    type: String,
    default: 'gray-100'
  }
})

const emit = defineEmits(['load', 'error', 'upload'])

const imageError = ref(false)
const fileInput = ref(null)

const containerClasses = computed(() => {
  const baseClasses = 'relative overflow-hidden border-2 border-dashed border-gray-300 transition-all duration-200'
  const roundedClasses = {
    none: '',
    sm: 'rounded-sm',
    md: 'rounded-md',
    lg: 'rounded-lg',
    xl: 'rounded-xl',
    full: 'rounded-full'
  }
  const interactiveClasses = props.editable ? 'cursor-pointer hover:border-gray-400 hover:bg-gray-50' : ''
  
  return `${baseClasses} ${roundedClasses[props.rounded]} ${interactiveClasses}`
})

const containerStyle = computed(() => {
  const width = typeof props.width === 'number' ? `${props.width}px` : props.width
  const height = typeof props.height === 'number' ? `${props.height}px` : props.height
  
  return {
    width,
    height,
    minWidth: width,
    minHeight: height
  }
})

const imageClasses = computed(() => {
  const baseClasses = 'w-full h-full'
  const objectFitClasses = {
    cover: 'object-cover',
    contain: 'object-contain',
    fill: 'object-fill',
    none: 'object-none',
    'scale-down': 'object-scale-down'
  }
  
  return `${baseClasses} ${objectFitClasses[props.objectFit]}`
})

const placeholderClasses = computed(() => {
  const baseClasses = 'w-full h-full flex items-center justify-center'
  const backgroundClasses = {
    'gray-100': 'bg-gray-100',
    'gray-50': 'bg-gray-50',
    'blue-50': 'bg-blue-50',
    'green-50': 'bg-green-50',
    'purple-50': 'bg-purple-50',
    'yellow-50': 'bg-yellow-50'
  }
  
  return `${baseClasses} ${backgroundClasses[props.backgroundColor] || 'bg-gray-100'}`
})

const handleImageLoad = (event) => {
  imageError.value = false
  emit('load', event)
}

const handleImageError = (event) => {
  imageError.value = true
  emit('error', event)
}

const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      emit('upload', {
        file,
        dataUrl: e.target.result
      })
    }
    reader.readAsDataURL(file)
  }
}

const handleClick = () => {
  if (props.editable && fileInput.value) {
    fileInput.value.click()
  }
}

// 监听容器点击事件
onMounted(() => {
  if (props.editable) {
    const container = getCurrentInstance().vnode.el
    container.addEventListener('click', handleClick)
    
    onUnmounted(() => {
      container.removeEventListener('click', handleClick)
    })
  }
})
</script>

<style scoped>
/* 深色主题支持 */
.dark .bg-gray-100 {
  @apply bg-gray-800;
}

.dark .bg-gray-50 {
  @apply bg-gray-900;
}

.dark .bg-blue-50 {
  @apply bg-blue-900/20;
}

.dark .bg-green-50 {
  @apply bg-green-900/20;
}

.dark .bg-purple-50 {
  @apply bg-purple-900/20;
}

.dark .bg-yellow-50 {
  @apply bg-yellow-900/20;
}

.dark .border-gray-300 {
  @apply border-gray-600;
}

.dark .hover\:border-gray-400:hover {
  @apply border-gray-500;
}

.dark .hover\:bg-gray-50:hover {
  @apply bg-gray-800;
}

.dark .text-gray-500 {
  @apply text-gray-400;
}

.dark .text-gray-400 {
  @apply text-gray-500;
}
</style>