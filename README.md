# SW3 Ⅲ - Conference Management System

## Structure Directory Description

```bash
├─public	// public files
│  └─image
└─src
    ├─api	// api doc
    │  └─login
    ├─assets	// private files
    │  ├─image
    │  └─style	// internal style
    ├─components	// components
    │  ├─footer
    │  ├─menu
    │  └─navbar
    ├─config	// config files
    ├─hooks	// hooks functions
    ├─layout	// pages layouts
    ├─locale	// i18n
    │  ├─en-US
    │  └─zh-CN
    ├─mock	// analog interface
    ├─router
    │  ├─guard	// router guard
    │  └─routes
    │      └─modules
    ├─store	// global state storage
    │  └─modules
    │      ├─app
    │      ├─grade
    │      ├─tab-bar
    │      └─user
    ├─types	// data type definition
    ├─utils	// tools functions
    └─views // views folders
        ├─home
        │  └─intro
        │      ├─components
        │      └─locale
        ├─login
        │  ├─components
        │  └─locale
        ├─luckydraw
        │  └─choose
        │      ├─components
        │      └─locale
        ├─not-found
        └─poster
            ├─edit
            │  ├─components
            │  └─locale
            ├─grade
            │  ├─components
            │  └─locale
            ├─show&vote
            │  ├─components
            │  └─locale
            └─upload
                ├─components
                └─locale
```

## Enviromnment Settings

Vue3+TS+Pinia

Based on **Arco Design Vue**

Yarn

## RUN

```bash
yarn
yarn dev
```
