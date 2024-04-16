"use strict";
(self["webpackChunkjupyterlab_notebook_autosave"] = self["webpackChunkjupyterlab_notebook_autosave"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var dayjs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! dayjs */ "webpack/sharing/consume/default/dayjs/dayjs");
/* harmony import */ var dayjs__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(dayjs__WEBPACK_IMPORTED_MODULE_2__);



const PLUGIN_ID = 'jupyterlab-notebook-autosave:plugin';
const extension = {
    id: PLUGIN_ID,
    description: 'A JupyterLab extension that will autosave your open Notebook.',
    autoStart: true,
    requires: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__.ISettingRegistry],
    activate: (app, settings) => {
        const { commands } = app;
        if (app.name === 'JupyterLab') {
            return;
        }
        function getSetting(settings, name) {
            return settings === null || settings === void 0 ? void 0 : settings[name];
        }
        function handleCustomSave() {
            commands
                .execute('docmanager:save', { origin: 'init' })
                .then(() => {
                var _a;
                const customSaveButton = document.querySelector('[data-command="custom:save"]');
                const saveInfoElement = document.getElementById('custom-save-info');
                const saveInfoElementContent = `Last saved: today ${dayjs__WEBPACK_IMPORTED_MODULE_2___default()().format('h:mm:ss A')}`;
                if (saveInfoElement) {
                    saveInfoElement.innerHTML = saveInfoElementContent;
                }
                else {
                    const newSaveInfoElement = document.createElement('span');
                    newSaveInfoElement.id = 'custom-save-info';
                    newSaveInfoElement.innerHTML = saveInfoElementContent;
                    (_a = customSaveButton === null || customSaveButton === void 0 ? void 0 : customSaveButton.parentElement) === null || _a === void 0 ? void 0 : _a.appendChild(newSaveInfoElement);
                }
            })
                .catch((reason) => {
                console.error(`An error occurred while saving.\n${reason}`);
            });
        }
        commands.addCommand('custom:save', {
            label: 'Save changes',
            iconLabel: 'Save changes',
            icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.saveIcon,
            execute: () => handleCustomSave()
        });
        Promise.all([app.restored, settings.load(PLUGIN_ID)])
            .then(() => {
            var _a, _b, _c, _d, _e;
            const docmanagerPlugin = (_a = settings === null || settings === void 0 ? void 0 : settings.plugins) === null || _a === void 0 ? void 0 : _a['@jupyterlab/docmanager-extension:plugin'];
            const autosavePlugin = (_b = settings === null || settings === void 0 ? void 0 : settings.plugins) === null || _b === void 0 ? void 0 : _b[PLUGIN_ID];
            const docmanagerAutosaveInterval = getSetting(docmanagerPlugin === null || docmanagerPlugin === void 0 ? void 0 : docmanagerPlugin.settings, 'autosaveInterval');
            const autosavePluginAutosaveInterval = getSetting(autosavePlugin === null || autosavePlugin === void 0 ? void 0 : autosavePlugin.settings, 'autosaveInterval');
            const autosavePluginAutosaveDefaultInterval = (_e = (_d = (_c = autosavePlugin === null || autosavePlugin === void 0 ? void 0 : autosavePlugin.schema) === null || _c === void 0 ? void 0 : _c.properties) === null || _d === void 0 ? void 0 : _d.autosaveInterval) === null || _e === void 0 ? void 0 : _e.default;
            const autosaveInterval = autosavePluginAutosaveInterval ||
                docmanagerAutosaveInterval ||
                autosavePluginAutosaveDefaultInterval;
            console.log(`Autosave interval: ${autosaveInterval} seconds`);
            setInterval(() => {
                handleCustomSave();
            }, autosaveInterval * 1000);
        })
            .catch(reason => {
            console.error(`Something went wrong when reading the settings.\n${reason}`);
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.3fd1a2fd12081d98e9fb.js.map