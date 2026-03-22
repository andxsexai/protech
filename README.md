# ПроТехСервис — Документация проекта
## Версия 1.0 | Тамбов, ул. Бастионная 24ж

---

## 📋 ИНФОРМАЦИЯ О ПРОЕКТЕ

| Параметр | Значение |
|----------|---------|
| Название | ПроТехСервис |
| Город | Тамбов |
| Адрес | ул. Бастионная 24ж |
| Telegram | @ProTehServis |
| ВКонтакте | https://vk.ru/club228452491 |
| Авито | https://www.avito.ru/brands/12ee3df534cdb6634639bf700d0796c2 |
| Оплата | https://app.lava.top/products/0ff47d11-a7be-40be-a29d-edfbcb06d7f0 |

---

## 🎨 ДИЗАЙН-СИСТЕМА

### Цвета (CSS Variables)
```css
--neon-green: #00ff41      /* Основной акцент */
--neon-cyan: #00d4ff       /* Вторичный акцент */
--neon-red: #ff0040        /* Предупреждения */
--neon-yellow: #ffff00     /* Цены, важное */
--bg-dark: #020c02         /* Фон */
--bg-panel: rgba(0,20,0,0.85)  /* Карточки */
--text-main: #c8ffc8       /* Основной текст */
--text-dim: #4a7a4a        /* Второстепенный */
```

### Шрифты (Google Fonts)
- **Orbitron** — заголовки, названия, логотип (weight: 400, 700, 900)
- **Share Tech Mono** — код, терминал, основной текст
- **Rajdhani** — описания (weight: 300, 400, 600, 700)

---

## 🏗 СТРУКТУРА ФАЙЛОВ

```
ProTehServis/
├── index.html          ← Главный файл (всё в одном)
├── README.md           ← Эта документация
└── assets/             ← Для медиафайлов (создать вручную)
    ├── videos/         ← Видео с телефонами (из папки ПроТехСервис)
    └── images/         ← Фото работ
```

---

## 📱 РАЗДЕЛЫ САЙТА

### 1. HERO (Главный экран)
- Матрица на canvas фоне (`#matrix-bg`)
- Молния следует за курсором (`#lightning-canvas`)
- Кастомный курсор с кодом-следом (`#cursor`)
- Анимированный заголовок с глитч-эффектом
- Счётчики: 1200+ ремонтов, 5 лет, 98%, 1 год гарантии

### 2. УСЛУГИ (#services)
8 карточек услуг. Каждая открывает модальное окно с деталями и ценами:
- 01 Ремонт телефонов → `openModal('phones')`
- 02 Планшеты → `openModal('tablets')`
- 03 Ноутбуки/ПК → `openModal('laptops')`
- 04 Игровые консоли → `openModal('consoles')`
- 05 Разблокировка → `openModal('unlock')`
- 06 EMMC/Автомузыка → `openModal('emmc')`
- 07 Мелкая техника → `openModal('small')`
- 08 Срочный ремонт → прямая ссылка в TG

### 3. ДИАГНОСТИКА (#diagnostic)
- Объяснение почему 500₽ (не бесплатно)
- Калькулятор экономии в стиле терминала
- Карточка оплаты с анимацией
- Кнопка → https://app.lava.top/products/0ff47d11-a7be-40be-a29d-edfbcb06d7f0

### 4. РЕЗУЛЬТАТЫ (#results)
8 папок с работами. Каждая открывает модальное окно:
- РЕБОЛЛИНГ (BGA) → `openModal('reballing')`
- СВАП HONOR → `openModal('swap-honor')`
- СВАП IPHONE → `openModal('swap-iphone')`
- РАЗБЛОКИРОВКА ICLOUD → `openModal('unlock-icloud')`
- УВЕЛИЧЕНИЕ ПАМЯТИ → `openModal('memory')`
- FRP ОБХОД → `openModal('frp')`
- ПЕРЕКАТ ПРОЦЕССОВ → `openModal('processes')`
- НАКАТКА РЕБОЛЛИНГ → `openModal('nakatta')`

### 5. ОТЗЫВЫ (#reviews)
- 6 отзывов в бесконечном скролле
- Дублированы для бесшовной прокрутки

### 6. ПАРТНЁРЫ (#partners)
- 10 брендов в бесконечном скролле
- Apple, Samsung, Xiaomi, PlayStation, Xbox, Huawei, Lenovo, HP, ASUS, Авито

### 7. КОНТАКТЫ (#contacts)
- Все ссылки: TG, VK, Авито, адрес, время работы
- Визуализация карты в хакерском стиле

---

## ⚡ ФУНКЦИИ JAVASCRIPT

```javascript
// Открыть модальное окно
openModal('phones')     // по ID секции

// Закрыть модальное окно
closeModal('phones')    // по ID секции

// Закрыть по Escape
// Закрыть кликом вне модала — встроено
```

---

## 🎬 КАК ДОБАВИТЬ ВИДЕО (Задача 3)

Видео из папки ПроТехСервис нужно добавить на главную как анимация.

### Вариант 1 — Видеослайдер в hero:
```html
<!-- Добавить перед closing </section> в hero -->
<div class="video-reel">
  <video autoplay muted loop playsinline>
    <source src="assets/videos/video1.mp4" type="video/mp4">
  </video>
  <!-- повторить для каждого видео -->
</div>
```

```css
.video-reel {
  display: flex; gap: 10px;
  overflow: hidden;
  margin-top: 40px;
  border: 1px solid rgba(0,255,65,0.2);
}
.video-reel video {
  height: 150px;
  border: 1px solid rgba(0,255,65,0.15);
  filter: saturate(0.7) brightness(0.8);
}
```

### Вариант 2 — Видео в модалках результатов:
```html
<!-- В любом modal-work-grid -->
<div class="modal-work-item">
  <video autoplay muted loop playsinline style="width:100%;height:120px;object-fit:cover;">
    <source src="assets/videos/reballing1.mp4" type="video/mp4">
  </video>
  <div class="work-title">Реболлинг Samsung</div>
</div>
```

---

## 💳 ПОДКЛЮЧЕНИЕ ОПЛАТЫ

### Текущая ссылка Lava:
```
https://app.lava.top/products/0ff47d11-a7be-40be-a29d-edfbcb06d7f0
```

### Где используется в коде:
1. Кнопка в секции `#diagnostic` → `.pay-btn`
2. Плавающий виджет `#floatPayment` (появляется при прокрутке 30%)
3. Ссылка в navbar (можно добавить)

### Добавить виджет Lava (если доступен):
```html
<!-- Вставить вместо простой ссылки -->
<script src="https://app.lava.top/widget.js"></script>
<div data-lava-product="0ff47d11-a7be-40be-a29d-edfbcb06d7f0"></div>
```

---

## 🔧 ЗАДАЧИ ДЛЯ CURSOR (дальнейшая работа)

### Задача A — Добавить реальные фото/видео:
1. Загрузить файлы в `assets/`
2. В модалках заменить `work-icon` на `<img>` или `<video>`
3. Добавить lightbox для полноэкранного просмотра

### Задача B — Интеграция отзывов из VK:
```javascript
// API VK для получения отзывов из группы
fetch(`https://api.vk.com/method/wall.get?owner_id=-228452491&count=10&access_token=TOKEN&v=5.131`)
  .then(r => r.json())
  .then(data => renderReviews(data.response.items))
```

### Задача C — Форма обратной связи:
```html
<div class="contact-form">
  <input type="text" placeholder="ИМЯ" class="form-input">
  <input type="tel" placeholder="ТЕЛЕФОН" class="form-input">
  <textarea placeholder="ОПИСАНИЕ ПРОБЛЕМЫ" class="form-input"></textarea>
  <button class="pay-btn" onclick="sendToTelegram()">ОТПРАВИТЬ ЗАЯВКУ</button>
</div>
```

### Задача D — Telegram Bot для заявок:
```javascript
async function sendToTelegram(data) {
  const BOT_TOKEN = 'YOUR_BOT_TOKEN';
  const CHAT_ID = 'YOUR_CHAT_ID';
  await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      chat_id: CHAT_ID,
      text: `🔧 НОВАЯ ЗАЯВКА\nИмя: ${data.name}\nТел: ${data.phone}\nПроблема: ${data.issue}`,
      parse_mode: 'HTML'
    })
  });
}
```

### Задача E — SEO оптимизация:
```html
<!-- Добавить в <head> -->
<meta name="description" content="Ремонт телефонов, ноутбуков, планшетов в Тамбове. ПроТехСервис — ул. Бастионная 24ж. Диагностика 500₽, гарантия на работы.">
<meta name="keywords" content="ремонт телефонов Тамбов, ремонт ноутбуков Тамбов, разблокировка телефона, FRP обход, реболлинг">
<meta property="og:title" content="ПроТехСервис | Ремонт техники в Тамбове">
<meta property="og:image" content="assets/images/og-image.jpg">
```

---

## 🎨 CSS КОМПОНЕНТЫ (для копирования в Cursor)

### Кнопка с эффектом сканирования:
```css
.scan-btn {
  position: relative; overflow: hidden;
  border: 2px solid var(--neon-green);
  color: var(--neon-green);
  background: transparent;
  padding: 12px 25px;
  font-family: 'Orbitron', monospace;
}
.scan-btn::before {
  content: '';
  position: absolute; top: 0; left: -100%;
  width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(0,255,65,0.3), transparent);
  animation: scan 2s linear infinite;
}
@keyframes scan { 0% {left:-100%} 100% {left:100%} }
```

### Карточка с неоновой границей:
```css
.neon-card {
  background: rgba(0,20,0,0.85);
  border: 1px solid rgba(0,255,65,0.15);
  transition: all 0.3s;
}
.neon-card:hover {
  border-color: rgba(0,255,65,0.5);
  box-shadow: 0 0 30px rgba(0,255,65,0.1);
  transform: translateY(-3px);
}
```

---

## 📊 СТРУКТУРА МОДАЛЬНОГО ОКНА

```html
<div class="modal-overlay" id="modal-ID">
  <div class="modal">
    <div class="modal-header">
      <div class="modal-title">ЗАГОЛОВОК</div>
      <button class="modal-close" onclick="closeModal('ID')">✕</button>
    </div>
    <!-- Контент -->
    <div class="modal-work-grid">
      <div class="modal-work-item">
        <span class="work-icon">🔧</span>
        <div class="work-title">Название работы</div>
        <div class="work-price">от XXX₽</div>
      </div>
    </div>
    <!-- ИЛИ -->
    <ul class="modal-content-list">
      <li>Пункт 1</li>
    </ul>
    <!-- CTA -->
    <a href="https://t.me/ProTehServis" class="pay-btn">→ Записаться</a>
  </div>
</div>
```

---

## ⚠️ ВАЖНЫЕ ЗАМЕТКИ

1. **Видео из папки ПроТехСервис** — нужно добавить вручную через `assets/videos/`
2. **Реальные фото результатов** — добавить в модалки результатов
3. **Плавающая оплата** — появляется автоматически при прокрутке 30% страницы
4. **Курсор кастомный** — всем элементам задан `cursor: none !important`
5. **Глитч на мобилке** — отключить при необходимости через `@media (max-width: 768px)`

---

## 🚀 ДЕПЛОЙ

### GitHub Pages (бесплатно):
```bash
git init
git add .
git commit -m "ПроТехСервис v1.0"
git remote add origin https://github.com/USERNAME/protehservis.git
git push -u origin main
# Settings → Pages → Source: main → /root
```

### Netlify (drag & drop):
1. Открыть netlify.com
2. Перетащить папку ProTehServis
3. Готово — получить ссылку

---

*Документация создана: 2024 | ПроТехСервис | Тамбов*
