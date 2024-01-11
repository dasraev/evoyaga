(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2bf3ba44"],{"2e00":function(e,t,l){"use strict";var a=l("7a23");const o={class:"text-2xl my-4"};function c(e,t,l,c,n,r){return Object(a["openBlock"])(),Object(a["createElementBlock"])("h1",o,[Object(a["renderSlot"])(e.$slots,"default")])}var n={name:"PageTitle"},r=l("d959"),s=l.n(r);const d=s()(n,[["render",c]]);t["a"]=d},8936:function(e,t,l){"use strict";var a=l("7a23");const o={class:"relative py-10 px-4 max-h-screen overflow-auto"},c=Object(a["createElementVNode"])("svg",{xmlns:"http://www.w3.org/2000/svg",class:"h-10 w-10",fill:"none",viewBox:"0 0 24 24",stroke:"currentColor"},[Object(a["createElementVNode"])("path",{"stroke-linecap":"round","stroke-linejoin":"round","stroke-width":"2",d:"M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"})],-1),n=[c];function r(e,t,l,c,r,s){return r.isOpen?(Object(a["openBlock"])(),Object(a["createElementBlock"])("div",{key:0,class:Object(a["normalizeClass"])(["absolute inset-0 z-10 overflow-hidden bg-gray-800 bg-opacity-50 py-[50px] flex items-center w-full",r.modalContentPosition]),onClick:t[2]||(t[2]=(...e)=>s.clickAwayHandlder&&s.clickAwayHandlder(...e))},[Object(a["createElementVNode"])("div",{class:Object(a["normalizeClass"])(["rounded-md bg-white shadow-sm overflow-y-auto",["center"===l.modalPosition?"w-[80%]":"w-[40%] h-screen",l.modalClass]]),onClick:t[1]||(t[1]=Object(a["withModifiers"])(()=>{},["stop"]))},[Object(a["createElementVNode"])("div",o,[l.hideCloseButton?Object(a["createCommentVNode"])("",!0):(Object(a["openBlock"])(),Object(a["createElementBlock"])("span",{key:0,class:"absolute clickEffectBtn right-1 top-1 cursor-pointer text-gray-300",onClick:t[0]||(t[0]=(...e)=>s.closeModal&&s.closeModal(...e))},n)),Object(a["renderSlot"])(e.$slots,"slotBody",{closeModal:s.closeModal})])],2)],2)):Object(a["createCommentVNode"])("",!0)}var s={props:{modalPosition:{type:String,default:"center",required:!0},closeOnClickAway:{type:Boolean,default:!0},hideCloseButton:{type:Boolean,default:!1},modalClass:{type:String}},data(){return{isOpen:!1,modalContentPosition:{"justify-center":"center"===this.modalPosition,"justify-end":"right"===this.modalPosition,"justify-start":"left"===this.modalPosition},modalContentMinWidth:{},externalData:void 0}},computed:{clickAwayHandlder(){return this.$props.closeOnClickAway?this.closeModal:null}},methods:{setExternalData(e){this.externalData=e},getExternalData(){return this.externalData},closeModal(){this.isOpen=!1},openModal(){this.isOpen=!0}}},d=l("d959"),i=l.n(d);const b=i()(s,[["render",r]]);t["a"]=b},d908:function(e,t,l){"use strict";l.r(t);var a=l("7a23"),o=l("451b");l("5779");const c={class:"min-w-full table-auto text-sm xl:text-base"},n=Object(a["createElementVNode"])("thead",null,[Object(a["createElementVNode"])("tr",{class:"bg-white border-b border-gray-300 text-gray-400"},[Object(a["createElementVNode"])("th",{class:"w-20 py-4"},"№"),Object(a["createElementVNode"])("th",{class:"text-left py-4 pl-3"},"Markaz nomi"),Object(a["createElementVNode"])("th",{class:"py-4 pl-3"},"Markaz joylashgan viloyat"),Object(a["createElementVNode"])("th",{class:"lg:w-1/12"}),Object(a["createElementVNode"])("th",{class:"lg:w-1/12"}),Object(a["createElementVNode"])("th",{class:"lg:w-1/12"})])],-1),r={class:"w-20 py-4"},s={class:"text-center"},d={class:"py-4 overflow-hidden overflow-ellipsis"},i={class:"flex items-center"},b={class:"text-center px-3 py-4"},u=Object(a["createElementVNode"])("td",null,null,-1),m=Object(a["createElementVNode"])("td",null,null,-1),p=Object(a["createElementVNode"])("td",null,null,-1);var j={__name:"TableCenters",props:{tableBody:{type:Array,required:!0},viewFor:{type:String}},emits:["see","edit","delete"],setup(e){return(e,t)=>(Object(a["openBlock"])(),Object(a["createElementBlock"])("table",c,[n,Object(a["createElementVNode"])("tbody",null,[(Object(a["openBlock"])(!0),Object(a["createElementBlock"])(a["Fragment"],null,Object(a["renderList"])(e.$props.tableBody,(e,t)=>(Object(a["openBlock"])(),Object(a["createElementBlock"])("tr",{key:e.id,class:"text-gray-800 odd:bg-white even:bg-grayPrimary rounded-3xl"},[Object(a["createElementVNode"])("td",r,[Object(a["createElementVNode"])("div",s,Object(a["toDisplayString"])(t+1),1)]),Object(a["createElementVNode"])("td",d,[Object(a["createElementVNode"])("div",i,Object(a["toDisplayString"])(e.name),1)]),Object(a["createElementVNode"])("td",b,Object(a["toDisplayString"])(e.region),1),u,m,p]))),128))])]))}};const O=j;var y=O,f=l("9062"),h=l.n(f),k=(l("e40d"),l("8936")),w=l("2e00");const x={key:1,class:"bg-white rounded-md p-[12px]"},v={class:"flex items-center justify-between py-[8px] px-[24px]"},g={class:"bg-primary text-white px-[12px] py-[6px] rounded-md"};var E={__name:"Centers",setup(e){const t=Object(a["ref"])(!0),l=Object(a["ref"])([]),c=Object(a["ref"])();function n(e){c.value.setExternalData(e),c.value.openModal()}return Object(a["onMounted"])(async()=>{t.value=!0;const{data:e}=await o["a"].get("/api/info/markazs/");l.value=e,t.value=!1}),(e,o)=>{const r=Object(a["resolveComponent"])("router-link");return Object(a["openBlock"])(),Object(a["createElementBlock"])(a["Fragment"],null,[t.value?(Object(a["openBlock"])(),Object(a["createBlock"])(Object(a["unref"])(h.a),{key:0,active:t.value,"onUpdate:active":o[0]||(o[0]=e=>t.value=e),"can-cancel":!1,"is-full-page":!0,color:"#4785FE",loader:"dots"},null,8,["active"])):(Object(a["openBlock"])(),Object(a["createElementBlock"])("div",x,[Object(a["createElementVNode"])("div",v,[Object(a["createVNode"])(Object(a["unref"])(w["a"]),null,{default:Object(a["withCtx"])(()=>[Object(a["createTextVNode"])(" Markazlar ro`yxati ")]),_:1}),Object(a["createElementVNode"])("button",g,[Object(a["createVNode"])(r,{to:"/addCenter"},{default:Object(a["withCtx"])(()=>[Object(a["createTextVNode"])(" Markaz qo'shish ")]),_:1})])]),Object(a["createVNode"])(Object(a["unref"])(y),{"table-body":l.value,onDelete:n},null,8,["table-body"])])),Object(a["createVNode"])(Object(a["unref"])(k["a"]),{ref_key:"modalComponentRef",ref:c,modalClass:"!w-1/2","modal-position":"center"},{slotBody:Object(a["withCtx"])(()=>[Object(a["createTextVNode"])(Object(a["toDisplayString"])(c.value.getExternalData().name),1)]),_:1},512)],64)}}};const N=E;t["default"]=N}}]);
//# sourceMappingURL=chunk-2bf3ba44.acef382b.js.map