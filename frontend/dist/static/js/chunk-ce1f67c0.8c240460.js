(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-ce1f67c0"],{"177e":function(e,t,a){"use strict";a.r(t);var n=a("7a23"),i=a("451b"),r=a("b7a4"),s=(a("14d9"),a("7bb1")),l=a("506a"),o=a("ceaa"),c=a("98c2"),u=a("6d74"),d=a("5a0c"),f=a.n(d),p=a("a5a1"),b=a("2061"),m=a("1f2e"),h=a("6605");const j={class:"grid grid-cols-3 gap-3 w-full lg:w-[85%]"},g={class:"form_wrapper my-3"},v=Object(n["createElementVNode"])("label",{class:"input_label",for:"last_name"}," Familiyasi ",-1),O={class:"error_message"},y={class:"form_wrapper my-3"},w=Object(n["createElementVNode"])("label",{class:"input_label",for:"first_name"}," Ismi ",-1),_={class:"error_message"},k={class:"form_wrapper my-3"},$=Object(n["createElementVNode"])("label",{class:"input_label",for:"father_name"}," Sharifi ",-1),V={class:"error_message"},M={class:"form_wrapper my-3"},D=Object(n["createElementVNode"])("label",{class:"input_label"}," Tug‘ilgan yili va sanasi ",-1),E={class:"error_message"},S={class:"form_wrapper my-3"},B=Object(n["createElementVNode"])("label",{class:"input_label",for:"position"}," Lavozimi ",-1),N={class:"error_message"},T={class:"form_wrapper my-3"},x=Object(n["createElementVNode"])("label",{class:"input_label",for:"position"}," Markaz - Tuman ",-1),L={class:"error_message"},R={class:"form_wrapper my-3"},I=Object(n["createElementVNode"])("label",{class:"input_label",for:"login"}," Login ",-1),F={class:"error_message"},U={class:"form_wrapper my-3"},C=Object(n["createElementVNode"])("label",{class:"input_label",for:"password"}," Parol ",-1),q={class:"error_message"},Y={class:"form_wrapper my-3"},z=Object(n["createElementVNode"])("label",{class:"input_label",for:"email"}," Email ",-1),A={class:"error_message"},H={class:"form_wrapper my-3"},W=Object(n["createElementVNode"])("label",{class:"input_label"}," Rasmi ",-1),P=Object(n["createElementVNode"])("div",{class:"flex justify-between shadow rounded w-full"},[Object(n["createElementVNode"])("p",{class:"flex items-center text-gray-400 px-3 overflow-hidden overflow-ellipsis base_input border-none"},"Rasmni yuklang"),Object(n["createElementVNode"])("span",{class:"flex px-4 items-center justify-center rounded bg-primary text-white tracking-wide text-sm cursor-pointer"}," YUKLASH ")],-1),J={class:"error_message"},Z=["disabled"],K=["disabled"];var G={__name:"AddWorkerToCenterMonitoringForm",props:{initialFields:{type:Object,default:function(){return null}},clearFormMode:{type:Boolean,default:!1},isEditMode:{type:Boolean,default:!1}},emits:["submit"],setup(e,{emit:t}){const a=e,i=4,r=Object(n["ref"])(!1),{handleSubmit:d,isSubmitting:G,resetForm:Q}=Object(s["b"])(),X=(Object(h["c"])(),Object(h["d"])()),{isEditMode:ee,clearFormMode:te}=Object(n["toRefs"])(a);Object(n["watch"])(()=>te.value,e=>{!0===e&&Q()});const{positionsList:ae}=Object(c["a"])(),{regionList:ne}=Object(u["a"])(),ie=Object(n["ref"])([]);function re({values:e,errors:t,results:a}){console.log(e),console.log(t),console.log(a)}const se=d(async({birth_date:e,position:a,...n})=>{const i={...n,groups:[a],birth_date:f()(e).format("YYYY-MM-DD")},r=new FormData;Object.keys(i).forEach(e=>{r.append(e,i[e])}),t("submit",r)},re),{value:le,errorMessage:oe}=Object(s["a"])("first_name",l["g"]().test(...Object(b["a"])()).required(b["d"])),{value:ce,errorMessage:ue}=Object(s["a"])("last_name",l["g"]().test(...Object(b["a"])()).required(b["d"])),{value:de,errorMessage:fe}=Object(s["a"])("father_name",l["g"]().test(...Object(b["a"])()).required(b["d"])),{value:pe,errorMessage:be}=Object(s["a"])("position",l["g"]().test(...Object(b["a"])()).required(b["d"])),{value:me,errorMessage:he}=Object(s["a"])("markaz_tuman",l["g"]().test(...Object(b["a"])()).required(b["d"])),{value:je,errorMessage:ge}=Object(s["a"])("birth_date",l["g"]().required(b["d"]),{initialValue:new Date(1990,0,1)}),{value:ve,errorMessage:Oe}=Object(s["a"])("password",l["g"]().required(b["d"]).min(8,Object(b["c"])({min:8}))),{value:ye,errorMessage:we}=Object(s["a"])("login",l["g"]().test(...Object(b["a"])()).required(b["d"])),{value:_e,errorMessage:ke}=Object(s["a"])("email",l["g"]().email("Email shaklida bo'lishi kerak").required(b["d"])),{value:$e,errorMessage:Ve}=Object(s["a"])("photo",l["d"]().nullable().required("Rasm yuklanishi shart"),{initialValue:null});return Object(n["watch"])(()=>me.value,()=>{console.log(me.value)}),Object(n["watch"])(()=>ae.value,e=>{e.length&&(pe.value=i)},{immediate:!0}),Object(n["watch"])(()=>pe.value,e=>{e!==i&&X.push({name:"add-worker-to-center",query:{position:pe.value}})}),(e,t)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("form",{onSubmit:t[10]||(t[10]=(...e)=>Object(n["unref"])(se)&&Object(n["unref"])(se)(...e))},[Object(n["createElementVNode"])("div",j,[Object(n["createElementVNode"])("div",g,[v,Object(n["withDirectives"])(Object(n["createElementVNode"])("input",{id:"last_name","onUpdate:modelValue":t[0]||(t[0]=e=>Object(n["isRef"])(ce)?ce.value=e:null),name:"last_name",class:"base_input",placeholder:"Familiyasini kiriting"},null,512),[[n["vModelText"],Object(n["unref"])(ce)]]),Object(n["createElementVNode"])("span",O,Object(n["toDisplayString"])(Object(n["unref"])(ue)),1)]),Object(n["createElementVNode"])("div",y,[w,Object(n["withDirectives"])(Object(n["createElementVNode"])("input",{id:"first_name","onUpdate:modelValue":t[1]||(t[1]=e=>Object(n["isRef"])(le)?le.value=e:null),name:"first_name",class:"base_input",placeholder:"Ismini kiriting"},null,512),[[n["vModelText"],Object(n["unref"])(le)]]),Object(n["createElementVNode"])("span",_,Object(n["toDisplayString"])(Object(n["unref"])(oe)),1)]),Object(n["createElementVNode"])("div",k,[$,Object(n["withDirectives"])(Object(n["createElementVNode"])("input",{id:"father_name","onUpdate:modelValue":t[2]||(t[2]=e=>Object(n["isRef"])(de)?de.value=e:null),name:"father_name",class:"base_input",placeholder:"Sharifini kiriting"},null,512),[[n["vModelText"],Object(n["unref"])(de)]]),Object(n["createElementVNode"])("span",V,Object(n["toDisplayString"])(Object(n["unref"])(fe)),1)]),Object(n["createElementVNode"])("div",M,[D,Object(n["createVNode"])(Object(n["unref"])(m["a"]),{modelValue:Object(n["unref"])(je),"onUpdate:modelValue":t[3]||(t[3]=e=>Object(n["isRef"])(je)?je.value=e:null),options:{maxDate:Object(n["unref"])(f.a)().subtract(18,"year").toDate(),startDate:Object(n["unref"])(f.a)().subtract(30,"year").toDate()}},null,8,["modelValue","options"]),Object(n["createElementVNode"])("span",E,Object(n["toDisplayString"])(Object(n["unref"])(ge)),1)]),Object(n["createElementVNode"])("div",S,[B,Object(n["createVNode"])(Object(n["unref"])(p["a"]),{disabled:r.value,id:"position",modelValue:Object(n["unref"])(pe),"onUpdate:modelValue":t[4]||(t[4]=e=>Object(n["isRef"])(pe)?pe.value=e:null),options:Object(n["unref"])(ae),"show-by":"name","track-by":"code",placeholder:"Lavozimni tanlang"},null,8,["disabled","modelValue","options"]),Object(n["createElementVNode"])("span",N,Object(n["toDisplayString"])(Object(n["unref"])(be)),1)]),Object(n["createElementVNode"])("div",T,[x,Object(n["createVNode"])(Object(n["unref"])(p["a"]),{id:"markaz_tuman",modelValue:Object(n["unref"])(me),"onUpdate:modelValue":t[5]||(t[5]=e=>Object(n["isRef"])(me)?me.value=e:null),options:Object(n["unref"])(ne),"show-by":"name","track-by":"id",placeholder:"Tumanni tanlang"},null,8,["modelValue","options"]),Object(n["createElementVNode"])("span",L,Object(n["toDisplayString"])(Object(n["unref"])(he)),1)]),Object(n["createElementVNode"])("div",R,[I,Object(n["withDirectives"])(Object(n["createElementVNode"])("input",{id:"login","onUpdate:modelValue":t[6]||(t[6]=e=>Object(n["isRef"])(ye)?ye.value=e:null),name:"login",class:"base_input",placeholder:"Login"},null,512),[[n["vModelText"],Object(n["unref"])(ye)]]),Object(n["createElementVNode"])("span",F,Object(n["toDisplayString"])(Object(n["unref"])(we)),1)]),Object(n["createElementVNode"])("div",U,[C,Object(n["withDirectives"])(Object(n["createElementVNode"])("input",{id:"password","onUpdate:modelValue":t[7]||(t[7]=e=>Object(n["isRef"])(ve)?ve.value=e:null),name:"password",class:"base_input",placeholder:"Yangi parol kiriting"},null,512),[[n["vModelText"],Object(n["unref"])(ve)]]),Object(n["createElementVNode"])("span",q,Object(n["toDisplayString"])(Object(n["unref"])(Oe)),1)]),Object(n["createElementVNode"])("div",Y,[z,Object(n["withDirectives"])(Object(n["createElementVNode"])("input",{id:"email","onUpdate:modelValue":t[8]||(t[8]=e=>Object(n["isRef"])(_e)?_e.value=e:null),name:"email",class:"base_input",placeholder:"Email misol: test@mail.ru"},null,512),[[n["vModelText"],Object(n["unref"])(_e)]]),Object(n["createElementVNode"])("span",A,Object(n["toDisplayString"])(Object(n["unref"])(ke)),1)]),Object(n["createElementVNode"])("div",H,[W,Object(n["createVNode"])(Object(n["unref"])(o["a"]),{id:"photo1",files:Object(n["unref"])($e),"onUpdate:files":t[9]||(t[9]=e=>Object(n["isRef"])($e)?$e.value=e:null),"multiple-files":!1,"initial-files":ie.value},{icon:Object(n["withCtx"])(()=>[P]),_:1},8,["files","initial-files"]),Object(n["createElementVNode"])("span",J,Object(n["toDisplayString"])(Object(n["unref"])(Ve)),1)])]),Object(n["unref"])(ee)?(Object(n["openBlock"])(),Object(n["createElementBlock"])("button",{key:0,class:"px-3 m-2 py-2 border bg-primary text-white rounded-md",type:"submit",disabled:Object(n["unref"])(G)},"Tahrirlashni tugatish",8,Z)):(Object(n["openBlock"])(),Object(n["createElementBlock"])("button",{key:1,type:"submit",disabled:Object(n["unref"])(G),class:"base_input bg-primary text-white border-primary"},"Saqlash",8,K))],32))}};const Q=G;var X=Q,ee=a("2e00"),te=a("e19e");const ae={class:"bg-white p-3 rounded-md"};var ne={__name:"AddWorkerToMonitoring",setup(e){const{alertIt:t}=Object(r["a"])(),a=Object(n["ref"])(!1),{alertThisError:s}=Object(te["a"])(),l=async e=>{try{const{data:n}=await i["a"].post("/auth/monitoring_user_create/",e);null!==n&&void 0!==n&&n.message&&await t(n.message),a.value=!0}catch(n){s(n)}};return(e,t)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",ae,[Object(n["createVNode"])(Object(n["unref"])(ee["a"]),null,{default:Object(n["withCtx"])(()=>[Object(n["createTextVNode"])(" Markazlarga monitoring xodimi qo'shish ")]),_:1}),Object(n["createVNode"])(Object(n["unref"])(X),{"clear-form-mode":a.value,onSubmit:l},null,8,["clear-form-mode"])]))}},ie=(a("a694"),a("d959")),re=a.n(ie);const se=re()(ne,[["__scopeId","data-v-4525f9b8"]]);t["default"]=se},2061:function(e,t,a){"use strict";a.d(t,"d",(function(){return n})),a.d(t,"e",(function(){return i})),a.d(t,"c",(function(){return r})),a.d(t,"b",(function(){return s})),a.d(t,"a",(function(){return l}));const n=({path:e})=>"Ushbu maydon to'ldirilishi shart",i=()=>"Xodimni belgilash zarur!",r=e=>`Ushbu maydon eng kami ${e.min} ta bo'lishi kerak`,s=e=>`Ushbu maydon eng ko'pi ${e.max} ta bo'lishi kerak`,l=e=>["is-latin","Iltimos faqat lotin harflaridan foydalaning",e=>{const t=/[^\P{L}a-z][^a-z]*/giu;return!t.test(e)}]},"2e00":function(e,t,a){"use strict";var n=a("7a23");const i={class:"text-2xl my-4"};function r(e,t,a,r,s,l){return Object(n["openBlock"])(),Object(n["createElementBlock"])("h1",i,[Object(n["renderSlot"])(e.$slots,"default")])}var s={name:"PageTitle"},l=a("d959"),o=a.n(l);const c=o()(s,[["render",r]]);t["a"]=c},"3c03":function(e,t,a){},"4b59":function(e,t,a){"use strict";var n=a("451b");const i={async fetchArrivedReasons(){return n["a"].get("api/juvenile/juveniles/arrived_reasons/")},async fetchMonitoringTypes(){return n["a"].get("api/juvenile/juveniles/monitoring_status/")},async fetchBasisDistributions(){return await n["a"].get("/api/juvenile/juveniles/basis_distributions/")},async fetchBringingReasonList(){return await n["a"].get("api/info/reason_bringing_child")},async fetchCharactersList(){return await n["a"].get("api/juvenile/juveniles/characters/")},async fetchConvictedTypesList(){return await n["a"].get("/api/juvenile/juveniles/convicted_lists/")},async fetchCountComeBack(){return await n["a"].get("api/juvenile/juveniles/get_came_back_center/")},async fetchCountries(){return await n["a"].get("api/info/countries/")},async fetchDeterminedLocations(){return await n["a"].get("/api/juvenile/juveniles/determined_locations/")},async fetchDistributionTypes(){return await n["a"].get("/api/juvenile/juveniles/distribution_types")},async fetchEducationTypes(){return await n["a"].get("/api/juvenile/juveniles/employment_education_types/")},async fetchGuardianshipTypes(){return await n["a"].get("/api/juvenile/juveniles/type_guardianships/")},async fetchHaveBeenInItmTypes(){return await n["a"].get("/api/juvenile/juveniles/have_been_in_itm_reasons/")},async fetchHaveBeenInRotmTypes(){return await n["a"].get("/api/juvenile/juveniles/have_been_in_rotm_reasons/")},async fetchHealthCareFacility(){return await n["a"].get("/api/juvenile/juveniles/type_healthcare_facility/")},async fetchInspectorTypesList(){return await n["a"].get("/api/juvenile/juveniles/inspector_types")},async fetchITMDirections(){return await n["a"].get("/api/juvenile/juveniles/itm_directions/")},async fetchJuvenileStatuses(){return await n["a"].get("api/juvenile/juveniles/juvenile_statuses")},async fetchLevelsKindship(){return await n["a"].get("api/juvenile/juveniles/level_kindships/")},async fetchMaritalStatuses(){return await n["a"].get("/api/juvenile/juveniles/marital_statuses/")},async fetchMarkazs(){return await(await n["a"].get("/api/info/markazs/"))},async fetchMasteryLevelList(){return await n["a"].get("api/juvenile/juveniles/mastery/")},async fetchMedicalListTypes(){return await n["a"].get("/api/info/medical_list/")},async fetchParentTypesList(){return await n["a"].get("/api/juvenile/juveniles/parent_types/")},async fetchPassportTypes(){return await n["a"].get("/api/juvenile/juveniles/passport_types/")},async fetchPositions(){return await n["a"].get("/auth/groups/")},async fetchROTMDirections(){return await n["a"].get("/api/juvenile/juveniles/rotm_types/")},async fetchSchoolTypes(){return await n["a"].get("/api/juvenile/juveniles/school_types")},async fetchSchoolsListByTypeAndRegionId(e,t){return await n["a"].get("/api/info/schools/ByTypeIdAndDistrictId/",{params:{school_type:e,district:t}})},async fetchKindergartens(e){return await n["a"].get("/api/info/kindergartens/ByDistrictId/",{params:{district:e.target.value}})},async fetchSchoolList(e){return await n["a"].get("/api/info/schools/ByDistrictId/",{params:{district:e.target.value}})},async fetchUniversitiesListByRegionId(e){return await n["a"].get("/api/info/universities/ByRegionId/",{params:{region:e.target.value}})},async fetchCollegesListByRegionId(e){return await n["a"].get("api/info/colleges/ByRegionId/",{params:{region:e.target.value}})},async fetchSpecialEducationListByRegionId(e){return await n["a"].get("/api/info/special_educations/ByRegionId/",{params:{region:e.target.value}})},async fetchVocationalSchoolsListByRegionId(e){return await n["a"].get("/api/info/vocational_schools/ByRegionId/",{params:{region:e.target.value}})},async fetchLitseysListByRegionId(e){return await n["a"].get("/api/info/litsey/ByRegionId/",{params:{region:e.target.value}})},async fetchTexnikumsListByRegionId(e){return await n["a"].get("/api/info/texnikums/ByRegionId/",{params:{region:e.target.value}})},async fetchSubBringingReasonList(e){return await n["a"].get("/api/info/subreasonbringing_child_by_parent/",{params:{parent:e.target.value}})},async fetchWhomGivenList(){return await n["a"].get("/api/juvenile/juveniles/foreign_to_whom_given/")},async fetchRegion(e){return await n["a"].get("/api/info/markaz_tumans/",{params:{region_id:e}})}};t["a"]=i},"5a0c":function(e,t,a){!function(t,a){e.exports=a()}(0,(function(){"use strict";var e=1e3,t=6e4,a=36e5,n="millisecond",i="second",r="minute",s="hour",l="day",o="week",c="month",u="quarter",d="year",f="date",p="Invalid Date",b=/^(\d{4})[-/]?(\d{1,2})?[-/]?(\d{0,2})[Tt\s]*(\d{1,2})?:?(\d{1,2})?:?(\d{1,2})?[.:]?(\d+)?$/,m=/\[([^\]]+)]|Y{1,4}|M{1,4}|D{1,2}|d{1,4}|H{1,2}|h{1,2}|a|A|m{1,2}|s{1,2}|Z{1,2}|SSS/g,h={name:"en",weekdays:"Sunday_Monday_Tuesday_Wednesday_Thursday_Friday_Saturday".split("_"),months:"January_February_March_April_May_June_July_August_September_October_November_December".split("_"),ordinal:function(e){var t=["th","st","nd","rd"],a=e%100;return"["+e+(t[(a-20)%10]||t[a]||t[0])+"]"}},j=function(e,t,a){var n=String(e);return!n||n.length>=t?e:""+Array(t+1-n.length).join(a)+e},g={s:j,z:function(e){var t=-e.utcOffset(),a=Math.abs(t),n=Math.floor(a/60),i=a%60;return(t<=0?"+":"-")+j(n,2,"0")+":"+j(i,2,"0")},m:function e(t,a){if(t.date()<a.date())return-e(a,t);var n=12*(a.year()-t.year())+(a.month()-t.month()),i=t.clone().add(n,c),r=a-i<0,s=t.clone().add(n+(r?-1:1),c);return+(-(n+(a-i)/(r?i-s:s-i))||0)},a:function(e){return e<0?Math.ceil(e)||0:Math.floor(e)},p:function(e){return{M:c,y:d,w:o,d:l,D:f,h:s,m:r,s:i,ms:n,Q:u}[e]||String(e||"").toLowerCase().replace(/s$/,"")},u:function(e){return void 0===e}},v="en",O={};O[v]=h;var y=function(e){return e instanceof $},w=function e(t,a,n){var i;if(!t)return v;if("string"==typeof t){var r=t.toLowerCase();O[r]&&(i=r),a&&(O[r]=a,i=r);var s=t.split("-");if(!i&&s.length>1)return e(s[0])}else{var l=t.name;O[l]=t,i=l}return!n&&i&&(v=i),i||!n&&v},_=function(e,t){if(y(e))return e.clone();var a="object"==typeof t?t:{};return a.date=e,a.args=arguments,new $(a)},k=g;k.l=w,k.i=y,k.w=function(e,t){return _(e,{locale:t.$L,utc:t.$u,x:t.$x,$offset:t.$offset})};var $=function(){function h(e){this.$L=w(e.locale,null,!0),this.parse(e)}var j=h.prototype;return j.parse=function(e){this.$d=function(e){var t=e.date,a=e.utc;if(null===t)return new Date(NaN);if(k.u(t))return new Date;if(t instanceof Date)return new Date(t);if("string"==typeof t&&!/Z$/i.test(t)){var n=t.match(b);if(n){var i=n[2]-1||0,r=(n[7]||"0").substring(0,3);return a?new Date(Date.UTC(n[1],i,n[3]||1,n[4]||0,n[5]||0,n[6]||0,r)):new Date(n[1],i,n[3]||1,n[4]||0,n[5]||0,n[6]||0,r)}}return new Date(t)}(e),this.$x=e.x||{},this.init()},j.init=function(){var e=this.$d;this.$y=e.getFullYear(),this.$M=e.getMonth(),this.$D=e.getDate(),this.$W=e.getDay(),this.$H=e.getHours(),this.$m=e.getMinutes(),this.$s=e.getSeconds(),this.$ms=e.getMilliseconds()},j.$utils=function(){return k},j.isValid=function(){return!(this.$d.toString()===p)},j.isSame=function(e,t){var a=_(e);return this.startOf(t)<=a&&a<=this.endOf(t)},j.isAfter=function(e,t){return _(e)<this.startOf(t)},j.isBefore=function(e,t){return this.endOf(t)<_(e)},j.$g=function(e,t,a){return k.u(e)?this[t]:this.set(a,e)},j.unix=function(){return Math.floor(this.valueOf()/1e3)},j.valueOf=function(){return this.$d.getTime()},j.startOf=function(e,t){var a=this,n=!!k.u(t)||t,u=k.p(e),p=function(e,t){var i=k.w(a.$u?Date.UTC(a.$y,t,e):new Date(a.$y,t,e),a);return n?i:i.endOf(l)},b=function(e,t){return k.w(a.toDate()[e].apply(a.toDate("s"),(n?[0,0,0,0]:[23,59,59,999]).slice(t)),a)},m=this.$W,h=this.$M,j=this.$D,g="set"+(this.$u?"UTC":"");switch(u){case d:return n?p(1,0):p(31,11);case c:return n?p(1,h):p(0,h+1);case o:var v=this.$locale().weekStart||0,O=(m<v?m+7:m)-v;return p(n?j-O:j+(6-O),h);case l:case f:return b(g+"Hours",0);case s:return b(g+"Minutes",1);case r:return b(g+"Seconds",2);case i:return b(g+"Milliseconds",3);default:return this.clone()}},j.endOf=function(e){return this.startOf(e,!1)},j.$set=function(e,t){var a,o=k.p(e),u="set"+(this.$u?"UTC":""),p=(a={},a[l]=u+"Date",a[f]=u+"Date",a[c]=u+"Month",a[d]=u+"FullYear",a[s]=u+"Hours",a[r]=u+"Minutes",a[i]=u+"Seconds",a[n]=u+"Milliseconds",a)[o],b=o===l?this.$D+(t-this.$W):t;if(o===c||o===d){var m=this.clone().set(f,1);m.$d[p](b),m.init(),this.$d=m.set(f,Math.min(this.$D,m.daysInMonth())).$d}else p&&this.$d[p](b);return this.init(),this},j.set=function(e,t){return this.clone().$set(e,t)},j.get=function(e){return this[k.p(e)]()},j.add=function(n,u){var f,p=this;n=Number(n);var b=k.p(u),m=function(e){var t=_(p);return k.w(t.date(t.date()+Math.round(e*n)),p)};if(b===c)return this.set(c,this.$M+n);if(b===d)return this.set(d,this.$y+n);if(b===l)return m(1);if(b===o)return m(7);var h=(f={},f[r]=t,f[s]=a,f[i]=e,f)[b]||1,j=this.$d.getTime()+n*h;return k.w(j,this)},j.subtract=function(e,t){return this.add(-1*e,t)},j.format=function(e){var t=this,a=this.$locale();if(!this.isValid())return a.invalidDate||p;var n=e||"YYYY-MM-DDTHH:mm:ssZ",i=k.z(this),r=this.$H,s=this.$m,l=this.$M,o=a.weekdays,c=a.months,u=function(e,a,i,r){return e&&(e[a]||e(t,n))||i[a].slice(0,r)},d=function(e){return k.s(r%12||12,e,"0")},f=a.meridiem||function(e,t,a){var n=e<12?"AM":"PM";return a?n.toLowerCase():n},b={YY:String(this.$y).slice(-2),YYYY:this.$y,M:l+1,MM:k.s(l+1,2,"0"),MMM:u(a.monthsShort,l,c,3),MMMM:u(c,l),D:this.$D,DD:k.s(this.$D,2,"0"),d:String(this.$W),dd:u(a.weekdaysMin,this.$W,o,2),ddd:u(a.weekdaysShort,this.$W,o,3),dddd:o[this.$W],H:String(r),HH:k.s(r,2,"0"),h:d(1),hh:d(2),a:f(r,s,!0),A:f(r,s,!1),m:String(s),mm:k.s(s,2,"0"),s:String(this.$s),ss:k.s(this.$s,2,"0"),SSS:k.s(this.$ms,3,"0"),Z:i};return n.replace(m,(function(e,t){return t||b[e]||i.replace(":","")}))},j.utcOffset=function(){return 15*-Math.round(this.$d.getTimezoneOffset()/15)},j.diff=function(n,f,p){var b,m=k.p(f),h=_(n),j=(h.utcOffset()-this.utcOffset())*t,g=this-h,v=k.m(this,h);return v=(b={},b[d]=v/12,b[c]=v,b[u]=v/3,b[o]=(g-j)/6048e5,b[l]=(g-j)/864e5,b[s]=g/a,b[r]=g/t,b[i]=g/e,b)[m]||g,p?v:k.a(v)},j.daysInMonth=function(){return this.endOf(c).$D},j.$locale=function(){return O[this.$L]},j.locale=function(e,t){if(!e)return this.$L;var a=this.clone(),n=w(e,t,!0);return n&&(a.$L=n),a},j.clone=function(){return k.w(this.$d,this)},j.toDate=function(){return new Date(this.valueOf())},j.toJSON=function(){return this.isValid()?this.toISOString():null},j.toISOString=function(){return this.$d.toISOString()},j.toString=function(){return this.$d.toUTCString()},h}(),V=$.prototype;return _.prototype=V,[["$ms",n],["$s",i],["$m",r],["$H",s],["$W",l],["$M",c],["$y",d],["$D",f]].forEach((function(e){V[e[1]]=function(t){return this.$g(t,e[0],e[1])}})),_.extend=function(e,t){return e.$i||(e(t,$,_),e.$i=!0),_},_.locale=w,_.isDayjs=y,_.unix=function(e){return _(1e3*e)},_.en=O[v],_.Ls=O,_.p={},_}))},"6d74":function(e,t,a){"use strict";a.d(t,"a",(function(){return r}));var n=a("7a23"),i=a("4b59");function r(){const e=Object(n["ref"])([]),t=async t=>{var a;console.log(t);let n=null;null!==t&&void 0!==t&&null!==(a=t.target)&&void 0!==a&&a.value&&(n=t.target.value);const{data:r}=await i["a"].fetchRegion(n);e.value=[...r]};return Object(n["onMounted"])(async()=>{await t()}),{regionList:e,fetchPositions:t}}},"98c2":function(e,t,a){"use strict";a.d(t,"a",(function(){return r}));var n=a("7a23"),i=a("4b59");function r(){const e=Object(n["ref"])([]),t=async()=>{const{data:t}=await i["a"].fetchPositions();e.value=t};return Object(n["onMounted"])(async()=>{await t()}),{positionsList:e}}},a694:function(e,t,a){"use strict";a("3c03")},ceaa:function(e,t,a){"use strict";var n=a("7a23"),i=a("5779");const r={class:"relative"},s=["href"],l={key:1,class:"absolute top-1 right-1 z-20"},o=["src"],c={class:"w-40 truncate"};var u={__name:"InputFileThumbWrapper",props:{fileType:{type:String},fileSource:{type:String},fileName:{type:String},isForDownload:{type:Boolean,default:!1},downloadPath:{type:String,default:""},disabled:{type:Boolean}},emits:["delete-file"],setup(e,{emit:t}){const a=e;return(u,d)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",r,[a.isForDownload?(Object(n["openBlock"])(),Object(n["createElementBlock"])("a",{key:0,target:"_blank",class:"absolute top-0 left-0 h-full z-10 w-full",href:a.downloadPath},null,8,s)):Object(n["createCommentVNode"])("",!0),e.disabled?Object(n["createCommentVNode"])("",!0):(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",l,[Object(n["createVNode"])(Object(n["unref"])(i["a"]),{icon:"mdi:close-box",class:"text-red-600 cursor-pointer",width:"32",onClick:d[0]||(d[0]=e=>t("delete-file",a.fileSource))})])),"image/jpeg"===e.fileType||"image/png"===e.fileType||"image/webp"===e.fileType||"image/gif"===e.fileType?(Object(n["openBlock"])(),Object(n["createElementBlock"])("img",{key:2,src:e.fileSource,class:"w-40 h-full object-cover",alt:""},null,8,o)):"application/pdf"===e.fileType?(Object(n["openBlock"])(),Object(n["createBlock"])(Object(n["unref"])(i["a"]),{key:3,class:"w-40 bg-gray-100",height:"100%",icon:"mdi:file-pdf-box"})):"application/vnd.openxmlformats-officedocument.wordprocessingml.document"===e.fileType?(Object(n["openBlock"])(),Object(n["createBlock"])(Object(n["unref"])(i["a"]),{key:4,class:"w-40 bg-gray-100",height:"100%",icon:"mdi:file-word"})):"application/vnd.ms-excel"===e.fileType||"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"===e.fileType?(Object(n["openBlock"])(),Object(n["createBlock"])(Object(n["unref"])(i["a"]),{key:5,class:"w-40 bg-gray-100",height:"100%",icon:"mdi:file-excel"})):(Object(n["openBlock"])(),Object(n["createBlock"])(Object(n["unref"])(i["a"]),{key:6,class:"w-40 bg-gray-100",height:"100%",icon:"mdi:file"})),Object(n["createElementVNode"])("p",c,Object(n["toDisplayString"])(e.fileName),1)]))}};const d=u;var f=d;const p=["disabled"],b={class:"flex mb-4"},m={class:""},h=["for"],j=["id","disabled"],g={class:""},v={key:0,class:"flex flex-wrap gap-4"},O={key:1,class:"flex flex-wrap gap-4"};var y={__name:"FileInput",props:{initialFiles:{type:Array,required:!1,default:function(){return[]}},id:{required:!0,type:String},files:{required:!0,validator:function(e){return-1!==["object"].indexOf(typeof e)}},multipleFiles:{type:Boolean,default:!1,required:!1},disabled:{type:Boolean}},emits:["file-upload","update:files","delete-initial-file"],setup(e,{emit:t}){const a=e,i=Object(n["ref"])([]),{files:r,multipleFiles:s,initialFiles:l}=Object(n["toRefs"])(a);function o(e,t){if(e.file=e,e.id="_"+Math.random().toString(36).substr(2,9),e&&!t){if(/(\/|^)(Thumbs\.db|desktop\.ini|\..+)$/.test(e.name))return;if(/\.(php5?|html?|jsx?)$/i.test(e.name))return;if(e&&e.file){let t=window.URL||window.webkitURL;t&&(e.blob=t.createObjectURL(e.file)),e.thumb="",e.blob&&"image/"===e.type.substr(0,6)&&(e.thumb=e.blob)}}return e}function c({target:e}){let a;a=s.value?r.value&&r.value.length?[...r.value,...e.files]:[...e.files]:e.files[0],t("update:files",a)}Object(n["watch"])(()=>l.value,e=>{e.length&&(i.value=e)});const u=Object(n["computed"])(()=>r.value&&r.value.length?r.value.map(e=>o(e)):r.value&&r.value.name?[o(r.value)]:[]);function d(e){r.value&&r.value.length?t("update:files",r.value.filter(t=>t.thumb!==e)):r.value&&r.value.name&&t("update:files",null)}function y(e){i.value=i.value.filter(t=>t.id!==e),t("delete-initial-file",e)}return(t,r)=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",{disabled:e.disabled},[Object(n["createElementVNode"])("div",b,[Object(n["createElementVNode"])("div",m,[Object(n["createElementVNode"])("label",{for:a.id},[Object(n["renderSlot"])(t.$slots,"icon")],8,h),Object(n["createElementVNode"])("input",{id:a.id,class:"hidden",type:"file",multiple:!0,accept:"image/png,image/gif,image/jpeg,image/webp,application/pdf,.doc,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document,.csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel",onInput:c,disabled:e.disabled},null,40,j)])]),Object(n["createElementVNode"])("div",g,[Object(n["unref"])(u)?(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",v,[(Object(n["openBlock"])(!0),Object(n["createElementBlock"])(n["Fragment"],null,Object(n["renderList"])(Object(n["unref"])(u),t=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",{key:t.id},[Object(n["createVNode"])(Object(n["unref"])(f),{disabled:e.disabled,"file-type":t.file.type,"file-source":t.thumb,"file-name":t.file.name,onDeleteFile:d},null,8,["disabled","file-type","file-source","file-name"])]))),128))])):Object(n["createCommentVNode"])("",!0),i.value.length?(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",O,[(Object(n["openBlock"])(!0),Object(n["createElementBlock"])(n["Fragment"],null,Object(n["renderList"])(i.value,t=>(Object(n["openBlock"])(),Object(n["createElementBlock"])("div",{key:t.name},[Object(n["createVNode"])(Object(n["unref"])(f),{disabled:e.disabled,"is-for-download":!0,"download-path":t.path,"file-type":t.type,"file-source":t.id,"file-name":t.name,onDeleteFile:y},null,8,["disabled","download-path","file-type","file-source","file-name"])]))),128))])):Object(n["createCommentVNode"])("",!0)])],8,p))}};const w=y;t["a"]=w},e19e:function(e,t,a){"use strict";a.d(t,"a",(function(){return i}));var n=a("b7a4");function i(){const{alertIt:e}=Object(n["a"])(),t=t=>{var a,n,i,r,s,l,o,c,u,d,f;if(console.log({error:t},"UseErrorAlert"),"string"===typeof(null===t||void 0===t||null===(a=t.response)||void 0===a||null===(n=a.data)||void 0===n?void 0:n.message))e(null===t||void 0===t||null===(d=t.response)||void 0===d||null===(f=d.data)||void 0===f?void 0:f.message,"error");else if(null!==t&&void 0!==t&&null!==(i=t.response)&&void 0!==i&&i.data&&"string"!==typeof(null===t||void 0===t||null===(r=t.response)||void 0===r?void 0:r.data)&&null!==t&&void 0!==t&&null!==(s=t.response)&&void 0!==s&&null!==(l=s.data)&&void 0!==l&&l.messages)Object.values(t.response.data.messages).map(t=>{null!==t&&void 0!==t&&t.message&&e(t.message,"error")});else if(Array.isArray(null===t||void 0===t||null===(o=t.response)||void 0===o?void 0:o.data)){var p;null===t||void 0===t||null===(p=t.response)||void 0===p||p.data.map(t=>{e(t,"error")})}else null!==t&&void 0!==t&&null!==(c=t.response)&&void 0!==c&&c.data&&400===(null===t||void 0===t||null===(u=t.response)||void 0===u?void 0:u.status)?Object.values(t.response.data).map(t=>{"string"==typeof t?e(t,"error"):t.map(t=>e(t,"error"))}):e("Server bilan bog'liq xatolik yuz berdi.","error")};return{alertThisError:t}}}}]);
//# sourceMappingURL=chunk-ce1f67c0.8c240460.js.map