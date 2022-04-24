<template>
  <div class="navbar">
    <div class="left-side">
      <a-space :size="-25">
        <img
          alt="logo"
          src="@/assets/image/logo.png"
          style="width: 50%"
        />
        <a-typography-title
          :style="{ margin: 0, fontSize: '18px' }"
          :heading="5"
        >
          UIC CMS
        </a-typography-title>
      </a-space>
    </div>
    <ul class="right-side">
      <li>
        <a-input-search
          :style="{width:'320px'}"
          :loading="isLoading"
          placeholder="Please enter"
          allow-clear
          v-if="isSearchShow"
          @change="onSearch"
          @search="onSearch"
        />
      </li>
      <li>
        <a-tooltip :content="t('settings.language')">
          <a-button
            class="nav-btn"
            type="outline"
            :shape="'circle'"
            @click="setDropDownVisible"
          >
            <template #icon>
              <icon-language />
            </template>
          </a-button>
        </a-tooltip>
        <a-dropdown trigger="click" @select="changeLocale">
          <div ref="triggerBtn" class="trigger-btn"></div>
          <template #content>
            <a-doption
              v-for="item in locales"
              :key="item.value"
              :value="item.value"
            >
              {{ item.label }}
            </a-doption>
          </template>
        </a-dropdown>
      </li>
      <li>
        <a-tooltip
          :content="
            theme === 'light'
              ? t('settings.navbar.theme.toDark')
              : t('settings.navbar.theme.toLight')
          "
        >
          <a-button
            class="nav-btn"
            type="outline"
            :shape="'circle'"
            @click="toggleTheme"
          >
            <template #icon>
              <icon-moon-fill v-if="theme === 'dark'" />
              <icon-sun-fill v-else />
            </template>
          </a-button>
        </a-tooltip>
      </li>
      <li>
        <a-dropdown trigger="click">
          <a-avatar
            :size="32"
            :style="{ marginRight: '8px', cursor: 'pointer' }"
          >
            <img alt="avatar" src="@/assets/image/avatar_user.jpg" />
          </a-avatar>
          <template #content>
            <a-doption>
              <a-space @click="handleLogout">
                <icon-export />
                <span>
                  {{ t('messageBox.logout') }}
                </span>
              </a-space>
            </a-doption>
          </template>
        </a-dropdown>
      </li>
    </ul>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue'
import { useDark, useToggle } from '@vueuse/core'
import { useI18n } from 'vue-i18n/index'
import useLocale from '@/hooks/locale'
import { LOCALE_OPTIONS } from '@/locale'
import useUser from '@/hooks/user'
import { useAppStore } from '@/store'
import { useRouter } from 'vue-router'
import { listenerRouteChange } from '@/utils/route-listener';

const isLoading = ref(false)
const isSearchShow = ref(false)
listenerRouteChange((newRoute) => {
  if(newRoute.name === 'show&vote'){
    isSearchShow.value = true
  } else {
    isSearchShow.value = false
  }
}, true)

const onSearch = (value: string) => {
  console.log(value)
}

const triggerBtn = ref()
const { changeLocale } = useLocale()
const locales = [...LOCALE_OPTIONS]
const { t } = useI18n()
const setDropDownVisible = () => {
  const event = new MouseEvent('click', {
    view: window,
    bubbles: true,
    cancelable: true,
  })
  triggerBtn.value.dispatchEvent(event)
}

const appStore = useAppStore()
const isDark = useDark({
  selector: 'body',
  attribute: 'arco-theme',
  valueDark: 'dark',
  valueLight: 'light',
  storageKey: 'arco-theme',
  onChanged(dark: boolean) {
    // overridded default behavior
    appStore.toggleTheme(dark)
  },
})

const router = useRouter()
const toggleTheme = useToggle(isDark)
const theme = computed(() => appStore.theme)
const { logout } = useUser()
const handleLogout = () => {
  logout(router, t)
}

</script>

<style scoped lang="less">
  .navbar {
    display: flex;
    justify-content: space-between;
    height: 100%;
    background-color: var(--color-bg-2);
    border-bottom: 1px solid var(--color-border);
  }

  .left-side {
    display: flex;
    align-items: center;
    padding-left: 20px;
  }

  .right-side {
    display: flex;
    padding-right: 20px;
    list-style: none;
    :deep(.locale-select) {
      border-radius: 20px;
    }
    li {
      display: flex;
      align-items: center;
      padding: 0 10px;
    }

    a {
      color: var(--color-text-1);
      text-decoration: none;
    }
    .nav-btn {
      border-color: rgb(var(--gray-2));
      color: rgb(var(--gray-8));
      font-size: 16px;
    }
    .trigger-btn,
    .ref-btn {
      position: absolute;
      bottom: 14px;
    }
    .trigger-btn {
      margin-left: 14px;
    }
  }
</style>

<style lang="less">
  .message-popover {
    .arco-popover-content {
      margin-top: 0;
    }
  }
</style>
