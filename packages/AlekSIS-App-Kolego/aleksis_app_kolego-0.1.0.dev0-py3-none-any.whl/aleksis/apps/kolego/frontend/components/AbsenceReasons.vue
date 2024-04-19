<script setup>
import InlineCRUDList from "aleksis.core/components/generic/InlineCRUDList.vue";
</script>

<template>
  <v-container>
    <inline-c-r-u-d-list
      :headers="headers"
      :i18n-key="i18nKey"
      create-item-i18n-key="kolego.absence_reason.create"
      :gql-query="gqlQuery"
      :gql-create-mutation="gqlCreateMutation"
      :gql-patch-mutation="gqlPatchMutation"
      :gql-delete-mutation="gqlDeleteMutation"
      :default-item="defaultItem"
    >
    </inline-c-r-u-d-list>
  </v-container>
</template>

<script>
import {
  absenceReasons,
  createAbsenceReasons,
  deleteAbsenceReasons,
  updateAbsenceReasons,
} from "./absenceReasons.graphql";

export default {
  name: "AbsenceReasons",
  data() {
    return {
      headers: [
        {
          text: this.$t("kolego.absence_reason.short_name"),
          value: "shortName",
        },
        {
          text: this.$t("kolego.absence_reason.name"),
          value: "name",
        },
      ],
      i18nKey: "kolego.absence_reason",
      gqlQuery: absenceReasons,
      gqlCreateMutation: createAbsenceReasons,
      gqlPatchMutation: updateAbsenceReasons,
      gqlDeleteMutation: deleteAbsenceReasons,
      defaultItem: {
        shortName: "",
        name: "",
      },
      required: [(value) => !!value || this.$t("forms.errors.required")],
    };
  },
};
</script>

<style scoped></style>
