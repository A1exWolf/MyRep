Vue.createApp({
    data: () => ({
        myHtml: '<h1>Vue 3 app</h1>',
        title: 'Я есть Грут',
        person: {
            firstName: 'Sasha',
            lastName: 'Volkov',
            age: 27
        },
        items: [1, 2]
    }),
    methods: {
        addItem(event) {
            this.items.unshift(this.$refs.myInput.value)
            this.$refs.myInput.value = ''
            console.log(event.key)
        },
        remove(i) {
            this.items.splice(i, 1)
        },
        log(item) {
            console.log(item)
        }
    },
    // methods: { Остановка скрипта при нажатия на этот элемент
    //     stopPropagation(event) {
    //         event.stopPropagation()
    //     }
    // }
    computed: {
        evenItems(){
            return this.items.filter(i => i % 2 == 0)
        }
    }
}).mount('#app')