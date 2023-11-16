(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-41c12991"],{"4b59":function(e,t,a){"use strict";var n=a("451b");const i={async fetchArrivedReasons(){return n["a"].get("api/juvenile/juveniles/arrived_reasons/")},async fetchMonitoringTypes(){return n["a"].get("api/juvenile/juveniles/monitoring_status/")},async fetchBasisDistributions(){return await n["a"].get("/api/juvenile/juveniles/basis_distributions/")},async fetchBringingReasonList(){return await n["a"].get("api/info/reason_bringing_child")},async fetchCharactersList(){return await n["a"].get("api/juvenile/juveniles/characters/")},async fetchConvictedTypesList(){return await n["a"].get("/api/juvenile/juveniles/convicted_lists/")},async fetchCountComeBack(){return await n["a"].get("api/juvenile/juveniles/get_came_back_center/")},async fetchCountries(){return await n["a"].get("api/info/countries/")},async fetchDeterminedLocations(){return await n["a"].get("/api/juvenile/juveniles/determined_locations/")},async fetchDistributionTypes(){return await n["a"].get("/api/juvenile/juveniles/distribution_types")},async fetchEducationTypes(){return await n["a"].get("/api/juvenile/juveniles/employment_education_types/")},async fetchGuardianshipTypes(){return await n["a"].get("/api/juvenile/juveniles/type_guardianships/")},async fetchHaveBeenInItmTypes(){return await n["a"].get("/api/juvenile/juveniles/have_been_in_itm_reasons/")},async fetchHaveBeenInRotmTypes(){return await n["a"].get("/api/juvenile/juveniles/have_been_in_rotm_reasons/")},async fetchHealthCareFacility(){return await n["a"].get("/api/juvenile/juveniles/type_healthcare_facility/")},async fetchInspectorTypesList(){return await n["a"].get("/api/juvenile/juveniles/inspector_types")},async fetchITMDirections(){return await n["a"].get("/api/juvenile/juveniles/itm_directions/")},async fetchJuvenileStatuses(){return await n["a"].get("api/juvenile/juveniles/juvenile_statuses")},async fetchLevelsKindship(){return await n["a"].get("api/juvenile/juveniles/level_kindships/")},async fetchMaritalStatuses(){return await n["a"].get("/api/juvenile/juveniles/marital_statuses/")},async fetchMarkazs(){return await(await n["a"].get("/api/info/markazs/"))},async fetchMasteryLevelList(){return await n["a"].get("api/juvenile/juveniles/mastery/")},async fetchMedicalListTypes(){return await n["a"].get("/api/info/medical_list/")},async fetchParentTypesList(){return await n["a"].get("/api/juvenile/juveniles/parent_types/")},async fetchPassportTypes(){return await n["a"].get("/api/juvenile/juveniles/passport_types/")},async fetchPositions(){return await n["a"].get("/auth/groups/")},async fetchROTMDirections(){return await n["a"].get("/api/juvenile/juveniles/rotm_types/")},async fetchSchoolTypes(){return await n["a"].get("/api/juvenile/juveniles/school_types")},async fetchSchoolsListByTypeAndRegionId(e,t){return await n["a"].get("/api/info/schools/ByTypeIdAndDistrictId/",{params:{school_type:e,district:t}})},async fetchKindergartens(e){return await n["a"].get("/api/info/kindergartens/ByDistrictId/",{params:{district:e.target.value}})},async fetchSchoolList(e){return await n["a"].get("/api/info/schools/ByDistrictId/",{params:{district:e.target.value}})},async fetchUniversitiesListByRegionId(e){return await n["a"].get("/api/info/universities/ByRegionId/",{params:{region:e.target.value}})},async fetchCollegesListByRegionId(e){return await n["a"].get("api/info/colleges/ByRegionId/",{params:{region:e.target.value}})},async fetchSpecialEducationListByRegionId(e){return await n["a"].get("/api/info/special_educations/ByRegionId/",{params:{region:e.target.value}})},async fetchVocationalSchoolsListByRegionId(e){return await n["a"].get("/api/info/vocational_schools/ByRegionId/",{params:{region:e.target.value}})},async fetchLitseysListByRegionId(e){return await n["a"].get("/api/info/litsey/ByRegionId/",{params:{region:e.target.value}})},async fetchTexnikumsListByRegionId(e){return await n["a"].get("/api/info/texnikums/ByRegionId/",{params:{region:e.target.value}})},async fetchSubBringingReasonList(e){return await n["a"].get("/api/info/subreasonbringing_child_by_parent/",{params:{parent:e.target.value}})},async fetchWhomGivenList(){return await n["a"].get("/api/juvenile/juveniles/foreign_to_whom_given/")},async fetchRegion(e){return await n["a"].get("/api/info/markaz_tumans/",{params:{region_id:e}})}};t["a"]=i},"7f24":function(e,t,a){"use strict";a("8bb4")},"8bb4":function(e,t,a){},"90a7":function(e,t,a){"use strict";var n=a("7a23");const i={class:"flex items-center gap-5"};function s(e,t,a,s,r,c){const o=Object(n["resolveComponent"])("GoBackBtn");return Object(n["openBlock"])(),Object(n["createElementBlock"])("div",i,[Object(n["createVNode"])(o),Object(n["createElementVNode"])("h1",null,[Object(n["renderSlot"])(e.$slots,"default")])])}const r=Object(n["createElementVNode"])("svg",{xmlns:"http://www.w3.org/2000/svg",class:"h-6 w-6 text-blue-400",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[Object(n["createElementVNode"])("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M11 17l-5-5m0 0l5-5m-5 5h12"})],-1),c=[r];function o(e,t,a,i,s,r){return Object(n["openBlock"])(),Object(n["createElementBlock"])("button",{class:"clickEffectBtn px-4 py-2",onClick:t[0]||(t[0]=t=>e.$router.back())},c)}var u={name:"GoBackBtn"},l=a("d959"),p=a.n(l);const g=p()(u,[["render",o]]);var v=g,d={name:"PageTitleWithGoBackButton",components:{GoBackBtn:v}};const y=p()(d,[["render",s]]);t["a"]=y},"98c2":function(e,t,a){"use strict";a.d(t,"a",(function(){return s}));var n=a("7a23"),i=a("4b59");function s(){const e=Object(n["ref"])([]),t=async()=>{const{data:t}=await i["a"].fetchPositions();e.value=t};return Object(n["onMounted"])(async()=>{await t()}),{positionsList:e}}},b8e2:function(e,t,a){"use strict";a.r(t);a("14d9");var n=a("7a23"),i=a("6605"),s=a("a5a1"),r=a("90a7"),c=a("98c2");const o=e=>(Object(n["pushScopeId"])("data-v-44381c58"),e=e(),Object(n["popScopeId"])(),e),u={class:"bg-white px-[20px] py-[16px]"},l={class:"p-2 grid grid-cols-3 gap-3 w-full lg:w-[85%]"},p={class:"form_wrapper my-3"},g=o(()=>Object(n["createElementVNode"])("label",{class:"input_label",for:"position"}," Lavozimi ",-1));var v={__name:"SelectWorkerPosition",setup(e){const t=Object(i["d"])(),a=2,o=3,{positionsList:v}=Object(c["a"])(),d=Object(n["ref"])("");return Object(n["watch"])(()=>d.value,()=>{console.log(d.value);const e=[a,o];e.includes(d.value)?t.push({name:"add-worker-to-center",query:{position:d.value}}):t.push({name:"add-worker-to-center-monitoring"})}),(e,t)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",u,[Object(n["createVNode"])(Object(n["unref"])(r["a"]),null,{default:Object(n["withCtx"])(()=>[Object(n["createTextVNode"])(" Markazga Xodim qo'shish ")]),_:1}),Object(n["createElementVNode"])("section",l,[Object(n["createElementVNode"])("div",p,[g,Object(n["createVNode"])(s["a"],{id:"position",modelValue:d.value,"onUpdate:modelValue":t[0]||(t[0]=e=>d.value=e),options:Object(n["unref"])(v),"show-by":"name","track-by":"code",placeholder:"Lavozimni tanlang"},null,8,["modelValue","options"])])])]))}},d=(a("7f24"),a("d959")),y=a.n(d);const h=y()(v,[["__scopeId","data-v-186c2a18"]]);t["default"]=h}}]);
//# sourceMappingURL=chunk-41c12991.53cf7b66.js.map