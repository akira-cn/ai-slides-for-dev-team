---
layout: section
---

# 第三部分

## AI 应用开发最佳实践

澄清常见误区，掌握核心开发模式

---
layout: default
---

# 💬 开放讨论

<div class="flex flex-col items-center space-y-8">
  <img 
    src="https://bot.hupox.com/resource/9r744efhue/45ec5b51829c43e29c8e6182bda8838d.png" 
    alt="AI应用开发讨论场景图" 
    class="max-w-lg w-full h-auto rounded-lg shadow-lg"
  />
  <h1 class="text-4xl font-bold text-gray-800 dark:text-white">
    你在AI应用开发中遇到过哪些困惑？
  </h1>
</div>

---
layout: default
---

# 🚫 常见误区澄清（1/3）

<div class="flex flex-col items-center space-y-4 mt-4">

<div class="bg-red-50 dark:bg-red-900/20 p-4 rounded-lg border-l-4 border-red-500 max-w-5xl w-full">
  <div class="flex items-center mb-3">
    <span class="text-xl mr-2">❌</span>
    <h3 class="text-lg font-bold text-red-700 dark:text-red-300">误区 1：大模型应用一定要训练/微调模型</h3>
  </div>
  
  <div class="grid grid-cols-2 gap-4">
    <div class="bg-white dark:bg-gray-800 p-3 rounded-lg shadow">
      <h4 class="font-bold text-red-600 dark:text-red-400 mb-2 text-sm flex items-center">
        <span class="text-sm mr-1">❌</span>
        错误认知
      </h4>
      <ul class="text-xs text-gray-700 dark:text-gray-300 space-y-1">
        <li class="flex items-start">
          <span class="w-1 h-1 bg-red-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>必须从零训练模型才能获得好效果</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-red-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>需要大量标注数据和计算资源</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-red-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>微调才能获得专业领域能力</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-red-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>预训练模型不够专业和准确</span>
        </li>
      </ul>
    </div>
    <div class="bg-white dark:bg-gray-800 p-3 rounded-lg shadow">
      <h4 class="font-bold text-green-600 dark:text-green-400 mb-2 text-sm flex items-center">
        <span class="text-sm mr-1">✅</span>
        正确做法
      </h4>
      <ul class="text-xs text-gray-700 dark:text-gray-300 space-y-1">
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>优先使用现有大模型API服务</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>通过Prompt Engineering优化效果</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>采用RAG检索增强生成技术</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>评估成本效益后才考虑微调</span>
        </li>
      </ul>
    </div>
  </div>
  
  <div class="mt-3 p-2 bg-blue-50 dark:bg-blue-900/20 rounded border border-blue-200 dark:border-blue-700">
    <div class="flex items-center mb-1">
      <span class="text-sm mr-1">💡</span>
      <h5 class="font-semibold text-blue-800 dark:text-blue-200 text-xs">实践建议</h5>
    </div>
    <p class="text-xs text-blue-700 dark:text-blue-300">
      80%的AI应用场景可以通过现有API + 精心设计的提示词解决，只有在特定领域需求无法满足时才考虑微调。
    </p>
  </div>

</div>

</div>

---
layout: default
---

# 🚫 常见误区澄清（2/3）

<div class="flex flex-col items-center space-y-4 mt-4">

<div class="bg-orange-50 dark:bg-orange-900/20 p-4 rounded-lg border-l-4 border-orange-500 max-w-5xl w-full">
  <div class="flex items-center mb-3">
    <span class="text-xl mr-2">❌</span>
    <h3 class="text-lg font-bold text-orange-700 dark:text-orange-300">误区 2：模型参数越大越好，小参数模型不值得部署</h3>
  </div>
  
  <div class="grid grid-cols-2 gap-4">
    <div class="bg-white dark:bg-gray-800 p-3 rounded-lg shadow">
      <h4 class="font-bold text-orange-600 dark:text-orange-400 mb-2 text-sm flex items-center">
        <span class="text-sm mr-1">❌</span>
        错误认知
      </h4>
      <ul class="text-xs text-gray-700 dark:text-gray-300 space-y-1">
        <li class="flex items-start">
          <span class="w-1 h-1 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>只有大参数模型效果才好</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>小模型能力有限，不值得使用</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>部署成本和响应速度不重要</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>追求最新最大的模型就是最好</span>
        </li>
      </ul>
    </div>
    <div class="bg-white dark:bg-gray-800 p-3 rounded-lg shadow">
      <h4 class="font-bold text-green-600 dark:text-green-400 mb-2 text-sm flex items-center">
        <span class="text-sm mr-1">✅</span>
        正确做法
      </h4>
      <ul class="text-xs text-gray-700 dark:text-gray-300 space-y-1">
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>根据具体场景选择合适模型</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>小模型在特定任务表现优异</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>综合考虑成本效益比</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>重视推理速度和用户体验</span>
        </li>
      </ul>
    </div>
  </div>
  
  <div class="mt-3 p-2 bg-blue-50 dark:bg-blue-900/20 rounded border border-blue-200 dark:border-blue-700">
    <div class="flex items-center mb-1">
      <span class="text-sm mr-1">💡</span>
      <h5 class="font-semibold text-blue-800 dark:text-blue-200 text-xs">实践建议</h5>
    </div>
    <p class="text-xs text-blue-700 dark:text-blue-300">
      选择模型时要平衡效果、成本、速度三个维度。很多场景下，7B参数的模型经过优化后效果不输175B模型。
    </p>
  </div>

</div>

</div>

---
layout: default
---

# 🚫 常见误区澄清（3/3）

<div class="flex flex-col items-center space-y-4 mt-4">

<div class="bg-purple-50 dark:bg-purple-900/20 p-4 rounded-lg border-l-4 border-purple-500 max-w-5xl w-full">
  <div class="flex items-center mb-3">
    <span class="text-xl mr-2">❌</span>
    <h3 class="text-lg font-bold text-purple-700 dark:text-purple-300">误区 3：企业大模型落地一定要建向量数据库</h3>
  </div>
  
  <div class="grid grid-cols-2 gap-4">
    <div class="bg-white dark:bg-gray-800 p-3 rounded-lg shadow">
      <h4 class="font-bold text-purple-600 dark:text-purple-400 mb-2 text-sm flex items-center">
        <span class="text-sm mr-1">❌</span>
        错误认知
      </h4>
      <ul class="text-xs text-gray-700 dark:text-gray-300 space-y-1">
        <li class="flex items-start">
          <span class="w-1 h-1 bg-purple-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>向量数据库是AI应用必需品</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-purple-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>所有企业知识都要向量化</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-purple-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>复杂的架构才显得专业</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-purple-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>检索增强是万能解决方案</span>
        </li>
      </ul>
    </div>
    <div class="bg-white dark:bg-gray-800 p-3 rounded-lg shadow">
      <h4 class="font-bold text-green-600 dark:text-green-400 mb-2 text-sm flex items-center">
        <span class="text-sm mr-1">✅</span>
        正确做法
      </h4>
      <ul class="text-xs text-gray-700 dark:text-gray-300 space-y-1">
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>评估是否真正需要RAG技术</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>简单场景优先用简单方案</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>采用渐进式架构演进策略</span>
        </li>
        <li class="flex items-start">
          <span class="w-1 h-1 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>灵活组合多种技术方案</span>
        </li>
      </ul>
    </div>
  </div>
  
  <div class="mt-3 p-2 bg-blue-50 dark:bg-blue-900/20 rounded border border-blue-200 dark:border-blue-700">
    <div class="flex items-center mb-1">
      <span class="text-sm mr-1">💡</span>
      <h5 class="font-semibold text-blue-800 dark:text-blue-200 text-xs">实践建议</h5>
    </div>
    <p class="text-xs text-blue-700 dark:text-blue-300">
      先用简单的API调用验证业务价值，确认需要知识检索后再考虑RAG，避免过度工程化。
    </p>
  </div>

</div>

</div>

---
layout: default
---

# 🎯 核心模式：以 LLM 为核心的一问一答

<div class="flex flex-col items-center space-y-4 mt-4">

<div class="bg-gradient-to-r from-blue-50 to-indigo-100 dark:from-blue-900/20 dark:to-indigo-900/20 p-4 rounded-xl shadow-lg max-w-6xl w-full">
  <div class="flex items-center mb-4">
    <span class="text-3xl mr-3">💬</span>
    <h3 class="text-xl font-bold text-blue-700 dark:text-blue-300">最简单直接的AI应用模式</h3>
  </div>
  
  <div class="grid grid-cols-3 gap-4">
    <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg">
      <h4 class="font-bold text-blue-600 dark:text-blue-400 mb-2 text-base flex items-center">
        <span class="text-lg mr-2">🎯</span>
        适用场景
      </h4>
      <ul class="text-gray-700 dark:text-gray-300 space-y-1 text-sm">
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>智能客服系统</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>内容生成工具</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>代码编程助手</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>多语言翻译</span>
        </li>
      </ul>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg">
      <h4 class="font-bold text-green-600 dark:text-green-400 mb-2 text-base flex items-center">
        <span class="text-lg mr-2">✅</span>
        核心优势
      </h4>
      <ul class="text-gray-700 dark:text-gray-300 space-y-1 text-sm">
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>开发简单快速</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>部署成本极低</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>响应速度快</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>维护成本低</span>
        </li>
      </ul>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg">
      <h4 class="font-bold text-orange-600 dark:text-orange-400 mb-2 text-base flex items-center">
        <span class="text-lg mr-2">⚠️</span>
        主要局限
      </h4>
      <ul class="text-gray-700 dark:text-gray-300 space-y-1 text-sm">
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>无状态记忆能力</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>复杂任务处理受限</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>缺乏外部工具调用</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>难以处理多步骤任务</span>
        </li>
      </ul>
    </div>
  </div>
  
  <div class="mt-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-700">
    <div class="flex items-center mb-1">
      <span class="text-base mr-2">💡</span>
      <h5 class="font-semibold text-blue-800 dark:text-blue-200 text-sm">最佳实践</h5>
    </div>
    <p class="text-xs text-blue-700 dark:text-blue-300">
      适合快速验证AI能力和业务价值的场景，是大多数团队入门AI应用开发的首选模式。
    </p>
  </div>

</div>

</div>

---
layout: default
---

# 🎯 核心模式：以 Workflow 为核心的结构化工作流

<div class="flex flex-col items-center space-y-4 mt-4">

<div class="bg-gradient-to-r from-green-50 to-emerald-100 dark:from-green-900/20 dark:to-emerald-900/20 p-4 rounded-xl shadow-lg max-w-6xl w-full">
  <div class="flex items-center mb-4">
    <span class="text-3xl mr-3">🔄</span>
    <h3 class="text-xl font-bold text-green-700 dark:text-green-300">可控可预测的AI处理流程</h3>
  </div>
  
  <div class="grid grid-cols-3 gap-4">
    <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg">
      <h4 class="font-bold text-green-600 dark:text-green-400 mb-2 text-base flex items-center">
        <span class="text-lg mr-2">🎯</span>
        适用场景
      </h4>
      <ul class="text-gray-700 dark:text-gray-300 space-y-1 text-sm">
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>数据处理流水线</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>内容审核系统</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>文档生成流程</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-green-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>业务流程自动化</span>
        </li>
      </ul>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg">
      <h4 class="font-bold text-blue-600 dark:text-blue-400 mb-2 text-base flex items-center">
        <span class="text-lg mr-2">✅</span>
        核心优势
      </h4>
      <ul class="text-gray-700 dark:text-gray-300 space-y-1 text-sm">
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>流程可控可预测</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>易于调试和优化</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>支持复杂业务逻辑</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>可视化流程管理</span>
        </li>
      </ul>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg">
      <h4 class="font-bold text-orange-600 dark:text-orange-400 mb-2 text-base flex items-center">
        <span class="text-lg mr-2">⚠️</span>
        主要局限
      </h4>
      <ul class="text-gray-700 dark:text-gray-300 space-y-1 text-sm">
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>缺乏动态决策能力</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>流程相对固化</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>需要预定义执行路径</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-orange-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>环境适应性有限</span>
        </li>
      </ul>
    </div>
  </div>
  
  <div class="mt-4 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg border border-green-200 dark:border-green-700">
    <div class="flex items-center mb-1">
      <span class="text-base mr-2">💡</span>
      <h5 class="font-semibold text-green-800 dark:text-green-200 text-sm">最佳实践</h5>
    </div>
    <p class="text-xs text-green-700 dark:text-green-300">
      适合有明确业务流程、需要稳定可靠输出的企业级应用场景，是规模化AI应用的重要模式。
    </p>
  </div>

</div>

</div>

---
layout: default
---

# 🎯 核心模式：以 Agent/Agentic 为核心的新一代智能体

<div class="flex flex-col items-center space-y-4 mt-4">

<div class="bg-gradient-to-r from-purple-50 to-violet-100 dark:from-purple-900/20 dark:to-violet-900/20 p-4 rounded-xl shadow-lg max-w-6xl w-full">
  <div class="flex items-center mb-4">
    <span class="text-3xl mr-3">🤖</span>
    <h3 class="text-xl font-bold text-purple-700 dark:text-purple-300">具备自主决策能力的智能系统</h3>
  </div>
  
  <div class="grid grid-cols-3 gap-4">
    <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg">
      <h4 class="font-bold text-purple-600 dark:text-purple-400 mb-2 text-base flex items-center">
        <span class="text-lg mr-2">🎯</span>
        适用场景
      </h4>
      <ul class="text-gray-700 dark:text-gray-300 space-y-1 text-sm">
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>智能个人助理</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>自动化运维系统</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>复杂问题求解</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-purple-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>多任务协调管理</span>
        </li>
      </ul>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg">
      <h4 class="font-bold text-blue-600 dark:text-blue-400 mb-2 text-base flex items-center">
        <span class="text-lg mr-2">✅</span>
        核心优势
      </h4>
      <ul class="text-gray-700 dark:text-gray-300 space-y-1 text-sm">
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>自主决策和规划</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>动态任务分解</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>丰富工具调用能力</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-blue-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>持续学习和优化</span>
        </li>
      </ul>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-lg shadow-lg">
      <h4 class="font-bold text-red-600 dark:text-red-400 mb-2 text-base flex items-center">
        <span class="text-lg mr-2">⚠️</span>
        主要挑战
      </h4>
      <ul class="text-gray-700 dark:text-gray-300 space-y-1 text-sm">
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-red-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>开发复杂度较高</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-red-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>行为难以完全预测</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-red-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>调试和监控困难</span>
        </li>
        <li class="flex items-start">
          <span class="w-1.5 h-1.5 bg-red-500 rounded-full mt-1.5 mr-2 flex-shrink-0"></span>
          <span>运行成本相对较高</span>
        </li>
      </ul>
    </div>
  </div>
  
  <div class="mt-4 p-3 bg-purple-50 dark:bg-purple-900/20 rounded-lg border border-purple-200 dark:border-purple-700">
    <div class="flex items-center mb-1">
      <span class="text-base mr-2">💡</span>
      <h5 class="font-semibold text-purple-800 dark:text-purple-200 text-sm">最佳实践</h5>
    </div>
    <p class="text-xs text-purple-700 dark:text-purple-300">
      代表AI应用的未来发展方向，适合需要高度智能化和自主性的复杂业务场景。
    </p>
  </div>

</div>

</div>

---
layout: default
---

<div class="mt-0">

<div class="bg-gradient-to-r from-gray-50 to-blue-50 dark:from-gray-800 dark:to-blue-900/20 p-4 rounded-xl mb-6">
  <h3 class="text-lg font-bold text-gray-800 dark:text-gray-200 mb-3 flex items-center">
    <span class="text-xl mr-2">🎯</span>
    如何选择合适的开发模式？
  </h3>
  
  <div class="grid grid-cols-3 gap-4">
    <div class="text-center">
      <div class="bg-blue-100 dark:bg-blue-900/30 p-3 rounded-lg mb-2">
        <span class="text-2xl">💬</span>
        <h4 class="font-bold text-blue-700 dark:text-blue-300 mt-1 text-sm">简单对话</h4>
      </div>
      <p class="text-xs text-gray-600 dark:text-gray-400">单轮问答<br/>快速响应<br/>成本敏感</p>
    </div>
    <div class="text-center">
      <div class="bg-green-100 dark:bg-green-900/30 p-3 rounded-lg mb-2">
        <span class="text-2xl">🔄</span>
        <h4 class="font-bold text-green-700 dark:text-green-300 mt-1 text-sm">结构化流程</h4>
      </div>
      <p class="text-xs text-gray-600 dark:text-gray-400">多步骤任务<br/>流程固定<br/>可控性要求高</p>
    </div>
    <div class="text-center">
      <div class="bg-purple-100 dark:bg-purple-900/30 p-3 rounded-lg mb-2">
        <span class="text-2xl">🤖</span>
        <h4 class="font-bold text-purple-700 dark:text-purple-300 mt-1 text-sm">智能体</h4>
      </div>
      <p class="text-xs text-gray-600 dark:text-gray-400">复杂决策<br/>动态规划<br/>自主性要求高</p>
    </div>
  </div>
</div>

<div class="bg-yellow-50 dark:bg-yellow-900/20 p-4 rounded-xl border border-yellow-200 dark:border-yellow-700">
  <div class="flex items-center mb-3">
    <span class="text-xl mr-2">💡</span>
    <h4 class="text-base font-bold text-yellow-800 dark:text-yellow-200">最佳实践建议</h4>
  </div>
  
  <div class="grid grid-cols-2 gap-4">
    <div>
      <h5 class="font-semibold text-yellow-700 dark:text-yellow-300 mb-1 text-sm">🚀 快速起步</h5>
      <ul class="text-xs text-gray-700 dark:text-gray-300 space-y-0.5">
        <li>• 从简单模式开始验证</li>
        <li>• 优先使用现有API服务</li>
        <li>• 重视用户体验和响应速度</li>
        <li>• 建立完善的监控体系</li>
      </ul>
    </div>
    <div>
      <h5 class="font-semibold text-yellow-700 dark:text-yellow-300 mb-1 text-sm">📈 渐进演进</h5>
      <ul class="text-xs text-gray-700 dark:text-gray-300 space-y-0.5">
        <li>• 根据业务需求逐步升级</li>
        <li>• 保持架构的灵活性</li>
        <li>• 持续优化成本效益比</li>
        <li>• 关注新技术发展趋势</li>
      </ul>
    </div>
  </div>
</div>

</div>

---
layout: center
class: text-center
---

# 小结

<div class="max-w-4xl mx-auto mt-8">

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
  
  <div class="bg-gradient-to-br from-red-50 to-orange-100 dark:from-red-900/20 dark:to-orange-900/20 p-6 rounded-xl shadow-lg border border-red-200 dark:border-red-700">
    <div class="flex items-center mb-3">
      <span class="text-2xl mr-3">🚫</span>
      <h4 class="text-lg font-bold text-red-800 dark:text-red-200">误区澄清</h4>
    </div>
    <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed !m-0">
       澄清了训练模型、参数大小、向量数据库等常见误区
     </p>
  </div>

  <div class="bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-blue-900/20 dark:to-indigo-900/20 p-6 rounded-xl shadow-lg border border-blue-200 dark:border-blue-700">
    <div class="flex items-center mb-3">
      <span class="text-2xl mr-3">💬</span>
      <h4 class="text-lg font-bold text-blue-800 dark:text-blue-200">LLM 对话模式</h4>
    </div>
    <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed !m-0">
       掌握了一问一答模式的适用场景和技术特点
     </p>
  </div>

  <div class="bg-gradient-to-br from-green-50 to-emerald-100 dark:from-green-900/20 dark:to-emerald-900/20 p-6 rounded-xl shadow-lg border border-green-200 dark:border-green-700">
    <div class="flex items-center mb-3">
      <span class="text-2xl mr-3">🔄</span>
      <h4 class="text-lg font-bold text-green-800 dark:text-green-200">工作流模式</h4>
    </div>
    <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed !m-0">
       了解了结构化工作流的设计原则和应用场景
     </p>
  </div>

  <div class="bg-gradient-to-br from-purple-50 to-violet-100 dark:from-purple-900/20 dark:to-violet-900/20 p-6 rounded-xl shadow-lg border border-purple-200 dark:border-purple-700">
    <div class="flex items-center mb-3">
      <span class="text-2xl mr-3">🤖</span>
      <h4 class="text-lg font-bold text-purple-800 dark:text-purple-200">智能体模式</h4>
    </div>
    <p class="text-sm text-gray-700 dark:text-gray-300 leading-relaxed !m-0">
        掌握了Agent/Agentic模式的核心能力和技术挑战
      </p>
  </div>

</div>

<div class="bg-gradient-to-r from-blue-500 to-purple-600 text-white p-6 rounded-xl shadow-xl">
  <h3 class="text-xl font-bold mb-2 flex items-center justify-center">
    <span class="text-2xl mr-3">🎯</span>
    下一步：构建高效的AI驱动团队
  </h3>
  <p class="text-blue-100 text-sm">探索AI时代的团队组织架构和协作模式</p>
</div>

</div>