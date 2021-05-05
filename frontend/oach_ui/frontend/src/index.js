import React, { Component } from "react";
import { render } from "react-dom";
import { v4 as uuidv4 } from "uuid";
import axios from "axios";
import Home from "./components/Home";
import Oach from "./components/Oach";

var evtSource = new EventSource(sessionData.cti_event_trans_params.RequestURL);
evtSource.onmessage = function(e) {
    try {
        let eventType = JSON.parse(e.data).event_sub_type;
        let msisdn = JSON.parse(e.data).input.split(";")[1].split("=")[1];
        let cust_accnt_id = "";
        let cust_accnt_number = "";
        if (["ONRINGING", "ONANSWER"].includes(eventType)) {
            let search_asset_pav_url = sessionData.search_asset_pav_trans_params.RequestURL;
            let search_asset_pav_auth = sessionData.search_asset_pav_trans_params.Authorization;
            let search_asset_pav_hdr_value = uuidv4().replaceAll("-", "");
            if (search_asset_pav_url) {
                search_asset_pav_url = search_asset_pav_url.replace("<PAV>", msisdn);
                axios.get(search_asset_pav_url, {
                    headers: {
                        "Authorization": search_asset_pav_auth,
                        "X-Oach-Request-Id": search_asset_pav_hdr_value
                    }
                })
                .then(function (response) {
                    if (response.status === 200) {
                        if (response.data.length > 0) {
                            cust_accnt_id = response.data[0].CustomerAccountId;
                            cust_accnt_number = response.data[0].CustomerAccountNumber;
                        }
                        if (eventType === "ONRINGING") {
                            toastr.options = {
                                "closeButton": false,
                                "debug": false,
                                "newestOnTop": false,
                                "progressBar": false,
                                "positionClass": "toast-top-center",
                                "preventDuplicates": true,
                                "onclick": null,
                                "showDuration": "300",
                                "hideDuration": "1000",
                                "timeOut": "5000",
                                "extendedTimeOut": "1000",
                                "showEasing": "swing",
                                "hideEasing": "linear",
                                "showMethod": "fadeIn",
                                "hideMethod": "fadeOut"
                            };
                            toastr["info"]("Incoming call from customer account # " + cust_accnt_number);
                        }
                        if (eventType === "ONANSWER" && cust_accnt_id) {
                            if ($('li[aria-labelledby="ui-id-470"]').attr("aria-selected") === "false") {
                                $('li[aria-labelledby="ui-id-470"]').addClass("siebui-active-navtab ui-tabs-active ui-state-active");
                                $('li[aria-labelledby="ui-id-470"]').attr("aria-selected", "true");
                                $('li[aria-labelledby="ui-id-470"]').attr("tabindex", "0");
                                $('li[aria-labelledby="ui-id-470"]').attr("aria-controls", "s_sctrl_tabScreen_noop");
                                $('li[aria-labelledby="ui-id-470"]').find("a").attr("aria-label", $(event.target).closest('li[role="tab"]').find("a").text().replace('"', '').trim() + " Selected");
                                $("div[id='OACH Overview'").css("display", "block");
                                if($('li[aria-labelledby="ui-id-469"]').attr("aria-selected") === "true") {
                                    $('li[aria-labelledby="ui-id-469"]').removeClass("siebui-active-navtab ui-tabs-active ui-state-active");
                                    $('li[aria-labelledby="ui-id-469"]').attr("aria-selected", "false");
                                    $('li[aria-labelledby="ui-id-469"]').attr("tabindex", "false");
                                    $('li[aria-labelledby="ui-id-469"]').removeAttr("aria-controls");
                                    $('li[aria-labelledby="ui-id-469"]').find("a").removeAttr("aria-label");
                                }
                                if ($("div[id='Home'").css("display") === "block") {
                                    $("div[id='Home'").css("display", "none");
                                }
                            }
                            $("input[name='search_account_number'").val("");
                            const oachDiv = document.getElementById("OACH Overview");
                            render(<Oach 
                                from_cti_search="True"
                                oach_account_id={cust_accnt_id}
                                oach_request_id={search_asset_pav_hdr_value} />, oachDiv);
                        }
                    }
                })
                .catch(function(error) {
                    console.error(error);
                });
            }
        }
    } catch (error) {
        console.error(error);
    }
}
evtSource.onerror = function(e) {
    console.log("Server closed event connection!");
}

const homeDiv = document.getElementById("Home");
const oachDiv = document.getElementById("OACH Overview");
render(<Home />, homeDiv);
render(<Oach 
    from_cti_search="False"/>, oachDiv);

document.getElementById("tb_0").scrollIntoView(); // Increase Profile Icon Size
$(document).on("click", function (event) { // Handle various click events
    try {
        
        if ($(event.target).attr("un") === "Logout") { // Logout
            location.href = "logout";
            return;
        }
        
        if ($(event.target).closest('span[id="s_0"]').attr("id") === "s_0") { // Menubar "Menu" button
            if($("#menu_overlay").css("display") === "none" && $("#ui-id-21").css("display") === "none") {
                $("#ui-id-21").css("display", "block");
                $("#menu_overlay").css("display", "block");
            } else {
                $("#ui-id-21").css("display", "none")
                $("#menu_overlay").css("display", "none")
            }
        }
        if ($(event.target).attr("id") === "menu_overlay") {
            if($("#menu_overlay").css("display") === "block" && $("#ui-id-21").css("display") === "block") {
                $("#ui-id-21").css("display", "none");
                $("#menu_overlay").css("display", "none");
            }
        }
        
        if ($(event.target).closest('li[id="tb_0"]').attr("id") === "tb_0") { // "Profile Toolbar popup"
            if($("#toolbar_overlay").css("display") === "none" && $("#toolbar_popup").css("display") === "none") {
                $("#toolbar_popup").css("display", "block");
                $("#toolbar_overlay").css("display", "block");
            } else {
                $("#toolbar_popup").css("display", "none")
                $("#toolbar_overlay").css("display", "none")
            }
        }
        if ($(event.target).attr("id") === "toolbar_overlay") {
            if($("#toolbar_overlay").css("display") === "block" && $("#toolbar_popup").css("display") === "block") {
                $("#toolbar_popup").css("display", "none");
                $("#toolbar_overlay").css("display", "none");
            }
        }
        
        let listOfTabIds = ["ui-id-469", "ui-id-470"]; // First Level View Bar
        let listOfComponents = ["Home", "OACH Overview"];
        let isPrimaryDivision = sessionData.primary_division
        if(listOfTabIds.includes($(event.target).closest('li[role="tab"]').attr("aria-labelledby"))) {
            if ($(event.target).closest('li[role="tab"]').attr("aria-labelledby") !== "ui-id-469") {
                if (!isPrimaryDivision) {
                    toastr.options = {
                        "closeButton": false,
                        "debug": false,
                        "newestOnTop": false,
                        "progressBar": false,
                        "positionClass": "toast-top-center",
                        "preventDuplicates": true,
                        "onclick": null,
                        "showDuration": "300",
                        "hideDuration": "1000",
                        "timeOut": "5000",
                        "extendedTimeOut": "1000",
                        "showEasing": "swing",
                        "hideEasing": "linear",
                        "showMethod": "fadeIn",
                        "hideMethod": "fadeOut"
                    };
                    toastr["error"]("Please select division first!");
                }
            }
            if ($(event.target).closest('li[role="tab"]').attr("aria-selected") === "false" && isPrimaryDivision) {
                let activeComponent = listOfComponents[listOfTabIds.indexOf($(event.target).closest('li[role="tab"]').attr("aria-labelledby"))];
                $(event.target).closest('li[role="tab"]').addClass("siebui-active-navtab ui-tabs-active ui-state-active");
                $(event.target).closest('li[role="tab"]').attr("aria-selected", "true");
                $(event.target).closest('li[role="tab"]').attr("tabindex", "0");
                $(event.target).closest('li[role="tab"]').attr("aria-controls", "s_sctrl_tabScreen_noop");
                $(event.target).closest('li[role="tab"]').find("a").attr("aria-label", $(event.target).closest('li[role="tab"]').find("a").text().replace('"', '').trim() + " Selected");
                $("div[id='" + activeComponent + "'").css("display", "block");
                let listOfOtherTabIds = listOfTabIds.filter(function(e) { return e !== $(event.target).closest('li[role="tab"]').attr("aria-labelledby") })
                let listOfOtherComponents = listOfComponents.filter(function(e) { return e !== activeComponent })
                for (let otherTab of listOfOtherTabIds) {
                    if($("li[aria-labelledby=" + otherTab + "]").attr("aria-selected") === "true") {
                        $("li[aria-labelledby=" + otherTab + "]").removeClass("siebui-active-navtab ui-tabs-active ui-state-active");
                        $("li[aria-labelledby=" + otherTab + "]").attr("aria-selected", "false");
                        $("li[aria-labelledby=" + otherTab + "]").attr("tabindex", "false");
                        $("li[aria-labelledby=" + otherTab + "]").removeAttr("aria-controls");
                        $("li[aria-labelledby=" + otherTab + "]").find("a").removeAttr("aria-label");
                        break;
                    }
                }
                for (let otherComponent of listOfOtherComponents) {
                    if ($("div[id='" + otherComponent + "'").css("display") === "block") {
                        $("div[id='" + otherComponent + "'").css("display", "none");
                    }
                }
            }
        }
    } catch(e) {
        console.error("Error: " + e.message);
    }
})
document.onkeydown = keydown; //Keyboard shortcuts
function keydown (evt) {
    if (!evt) evt = event;
    if (evt.ctrlKey && evt.shiftKey && evt.key === 'X') {
        location.href = "logout";
    }
}