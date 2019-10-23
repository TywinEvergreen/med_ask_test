<template>
    <div>
        <h1>Проверка услуг медицинского страхования</h1>

        <div style="margin-bottom: 3%">
            <mu-button v-if="data.insurance_type === 'MANDATORY'" disabled>ОМС</mu-button>
            <mu-button v-else color="#ED462F">ОМС</mu-button>
            <mu-button v-if="data.insurance_type === 'VOLUNTARY'" disabled>ДМС</mu-button>
            <mu-button v-else color="#ED462F">ДМС</mu-button>
        </div>

        <mu-row>
            <mu-col span="6" style="margin-right: 8.2%">
                <md-field>
                    <label>
                        <small>Введите номер полиса</small>
                    </label>
                    <md-input v-model="data.polis.identification_number" readonly></md-input>
                    <div class="md-helper-text"><strong>Дата окончания {{data.polis.expiration_date}}</strong></div>
                </md-field>
            </mu-col>

            <mu-col span="5">
                <md-field>
                    <label>
                        <small>Выберите страховую компанию</small>
                    </label>
                    <md-input v-model="data.insurance_company.title" readonly></md-input>
                    <div class="md-helper-text"><strong>Телефон {{data.insurance_company.phone_number}}</strong></div>
                </md-field>
            </mu-col>
        </mu-row>

        <br/>
        <h2 align="left">Выберите медицинские услуги</h2>

        <md-field>
            <label>
                <small>Выберите запрашиваемую услугу для пациента</small>
            </label>
            <md-input readonly></md-input>
        </md-field>

        <br/>

        <mu-row>
            <mu-col span="6">
                <h4 v-for="x in data.affordable"><img src="../assets/galochka.png" height="20" width="20"/> {{x}}</h4>
            </mu-col>
            <mu-col span="6">
                <h4 v-for="x in data.unaffordable"><img src="../assets/stop.png" height="20" width="20"/> {{x}}</h4>
                <h4 v-for="x in data.nonexistent"><img src="../assets/vopros.png" height="20" width="20"/> {{x}}</h4>
            </mu-col>
        </mu-row>

        <br />
        <br />

        <mu-button @click="goChecker" color="#65CFC4">Новый запрос</mu-button>
    </div>
</template>

<script>
    export default {
        name: "Results",
        data() {
            return {
                data: this.$route.params.data,
            }
        },
        created() {
            if (this.data === '') {
                this.$router.push({"name": "medical_services_checker"})
            }
        },
        methods: {
            goChecker() {
                this.$router.push({"name": "medical_services_checker"})
            }
        }
    }
</script>

<style scoped>
    .md-autocomplete, .md-field {
        box-shadow: 0.5px 1px 1.5px;
        border-radius: 2px;
    }

    .md-content {
        width: 80px;
        height: 60px;
        margin: 24px;
        box-shadow: 0 0 5px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
