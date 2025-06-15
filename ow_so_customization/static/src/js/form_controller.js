/** @odoo-module **/

import { Component } from "@odoo/owl";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { registry } from "@web/core/registry";
import { STATIC_ACTIONS_GROUP_NUMBER } from "@web/search/action_menus/action_menus";
import { useService } from "@web/core/utils/hooks";


const cogMenuRegistry = registry.category("cogMenu");

export class CustomAction extends Component {
    setup() {
        this.action = useService("action");
    }
    static template = "web.CustomAction";
    static components = { DropdownItem };

    async onClick() {
        this.action.doAction(
            {
                type: "ir.actions.act_window",
                target: "new",
                name: "Sales Order Report",
                res_model: "sales.report",
                views: [[false, "form"]],
            })
    }
}

export const CustomActionItem = {
   Component: CustomAction,
   groupNumber: STATIC_ACTIONS_GROUP_NUMBER,
   isDisplayed: async (env) =>
       env.config.viewType === "list" &&
       !env.model.root.selection.length && 
       env.searchModel.resModel === 'sale.order'
};

cogMenuRegistry.add("custom-action-menu", CustomActionItem, { sequence: 19 });