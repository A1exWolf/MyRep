const App = {
    data() {
        return {
            title: "Список заметок",
            placeholderString: 'Введите название заметки'
        }
    }
}

Vue.createApp(App).mount('#app')