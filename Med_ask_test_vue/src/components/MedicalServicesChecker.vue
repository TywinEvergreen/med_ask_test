<template>
    <div>
        <h1>Проверка услуг медицинского страхования</h1>

        <div style="margin-bottom: 3%">
            <mu-button v-if="form.insurance_type === 'MANDATORY'" disabled>ОМС</mu-button>
            <mu-button v-else color="#ED462F" @click="form.insurance_type = 'MANDATORY'">ОМС</mu-button>
            <mu-button v-if="form.insurance_type === 'VOLUNTARY'" disabled>ДМС</mu-button>
            <mu-button v-else color="#ED462F" @click="form.insurance_type = 'VOLUNTARY'">ДМС</mu-button>
        </div>

        <mu-row>
            <mu-col span="6" style="margin-right: 8.2%">
                <md-field>
                    <label>
                        <small>Введите номер полиса</small>
                    </label>
                    <md-input v-if="!polis_has_been_found" v-model="form.identificator" @change="getPolis"
                              maxlength="12"></md-input>
                    <md-input v-else v-model="form.identificator" readonly></md-input>
                </md-field>
            </mu-col>

            <mu-col span="5">
                <md-autocomplete v-model="form.insurance_company" :md-options="insurance_companies.map(x=>({
                             'logo_slug': x.logo_slug,
                             'title': x.title,
                             'toLowerCase':()=>x.title.toLowerCase(),
                             'toString':()=>x.title,}))">
                    <label>
                        <small>Выберите страховую компанию</small>
                    </label>
                    <template slot="md-autocomplete-item" slot-scope="{ item }">
                        <md-avatar>
                            <img :src="item.logo_slug" :alt="item.logo_slug">
                        </md-avatar>
                        <a>{{item.title}}</a>
                    </template>
                </md-autocomplete>
            </mu-col>
        </mu-row>

        <br/>
        <h2 align="left">Выберите медицинские услуги</h2>

        <md-autocomplete v-model="form.medical_service" @md-selected="choseMedicalService()" :md-options="medical_services.map(x=>({
                         'title': x.title,
                         'toLowerCase':()=>x.title.toLowerCase(),
                         'toString':()=>x.title,}))">
            <label>
                <small>Выберите запрашиваемую услугу для пациента</small>
            </label>
            <template slot="md-autocomplete-item" slot-scope="{ item }">
                <a>{{item.title}}</a>
            </template>
            <a @click="choseMedicalService()">Добавить</a>
        </md-autocomplete>

        <br/>

        <mu-row>
            <mu-col span="6" v-for="medical_service in chosen_medical_services" style="margin-bottom: 10px">
                {{medical_service}}
                <a @click="removeMedicalService(medical_service)">
                    <img src="../assets/krestik.png" height="20" width="20"/>
                </a>
            </mu-col>
        </mu-row>


        <mu-button
            v-if="form.identificator !== '' & form.insurance_company !== '' & chosen_medical_services.length !== 0"
            color="#ED462F" @click="checkMedicalServices">Проверить
        </mu-button>
        <mu-button v-else disabled>Проверить</mu-button>


        <transition name="fade">
            <div v-if="show_polis_not_found_error_message" class="popup-fade">
                <div class="popup" style="border-radius: 15px">
                    <h5>Полис с таким номером не обнаружен</h5>
                    <mu-button @click="show_polis_not_found_error_message = !show_polis_not_found_error_message"
                               color="#ED462F">Ок
                    </mu-button>
                </div>
            </div>
        </transition>
        <transition name="fade">
            <div v-if="show_already_chosen_error_message" class="popup-fade">
                <div class="popup" style="border-radius: 15px">
                    <h5>Вы уже добавили эту услугу</h5>
                    <mu-button @click="show_already_chosen_error_message = !show_already_chosen_error_message"
                               color="#ED462F">Ок
                    </mu-button>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
    export default {
        name: "PolisChecker",
        data() {
            return {
                fruits: ['Бенедикт', 'Камбербетч'],
                polis: Object,
                polis_has_been_found: false,
                insurance_companies: Array,
                medical_services: [],
                chosen_medical_services: [],
                show_polis_not_found_error_message: false,
                show_already_chosen_error_message: false,
                form: {
                    identificator: '',
                    insurance_company: '',
                    insurance_type: '',
                    medical_service: '',
                }
            }
        },
        mounted() {
            this.getInsuranceCompanies();
            this.getMedicalServices()
        },
        methods: {
            getPolis() {  // Получает полис по его номеру
                $.ajax({
                    url: this.$root.BACKEND_URL + "api/polis/",
                    type: "GET",
                    data: {
                        identificator: this.form.identificator,
                    },
                    success: (response => {
                        if (response.data.has_been_found) {
                            this.polis = response.data.data;
                            this.form.insurance_type = response.data.data.type;
                            this.polis_has_been_found = true;
                            this.form.insurance_company = response.data.data.insurance_company.title  // Строка передается вместо объекта для корректного отображения в форме
                        }
                    })
                })
            },
            checkMedicalServices() {
                if (!this.form.insurance_company.title) { // Страховая компания всегда должна быть объектом и содержать поле title, ведь при автозаполнении формы всегда передается {объект}
                    this.form.insurance_company = {title: this.form.insurance_company}
                }
                $.ajax({
                    url: this.$root.BACKEND_URL + "api/medical_services/check/",
                    type: "POST",
                    data: {
                        identificator: this.form.identificator,
                        insurance_company: this.form.insurance_company.title,
                        insurance_type: this.form.insurance_type,
                        chosen_medical_services: this.chosen_medical_services,
                    },
                    success: (response => {
                        console.log(response);
                        if (!response.data.polis_has_been_found) {
                            this.show_polis_not_found_error_message = true;  // Показывает сообщение ошибке
                            this.form.identificator = ''
                        } else {
                            this.$router.push({name: 'results', params: {"data": response.data}})
                        }
                    })
                })
            },
            getInsuranceCompanies() { // Получает полный список страховых компаний, для возможности их вывода в autocomplete
                $.ajax({
                    url: this.$root.BACKEND_URL + "api/insurance_companies/list/",
                    type: "GET",
                    success: (response => {
                        this.insurance_companies = response.data.data
                    })
                })
            },
            getMedicalServices() { // Получает полный список медуслуг, для возможности их вывода в autocomplete
                $.ajax({
                    url: this.$root.BACKEND_URL + "api/medical_services/list/",
                    type: "GET",
                    success: (response => {
                        this.medical_services = response.data.data
                    })
                })
            },
            choseMedicalService() {
                if (!this.form.medical_service.title) {
                    this.form.medical_service = {title: this.form.medical_service}; // Медуслуга должна быть объектом и содержать поле title
                }
                if (!this.chosen_medical_services.includes(this.form.medical_service.title)) {  // Проверяет, не выбрана ли услуга
                    this.chosen_medical_services.push(this.form.medical_service.title);  // Выбирает услугу
                } else {
                    this.show_already_chosen_error_message = true  // Показывает сообщение об ошибке
                }
                this.form.medical_service = '' // 'Очищает' форму
            },
            removeMedicalService(medical_service) {
                this.chosen_medical_services = this.chosen_medical_services.filter(v => v !== medical_service); // Создает новый массив, перебирая предыдущий, но без учета удаляемого элемента
            }
        }
    }
</script>

<style scoped>

    .fade-enter, .fade-leave-to {
        opacity: 0;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .3s;
    }

    .popup-fade:before {
        content: '';
        background: #000;
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        opacity: 0.3;
        z-index: 9999;
    }

    .popup {
        position: fixed;
        top: 25%;
        left: 50%;
        padding: 20px;
        width: 20%;
        margin-left: -10%;
        background: #fff;
        box-shadow: 0.5px 1px 1.5px #504c4c;
        border-radius: 4px;
        z-index: 99999;
        opacity: 1;
    }
</style>
