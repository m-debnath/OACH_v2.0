import React, { Component } from "react";
import axios from "axios";
import { makeStyles } from '@material-ui/core/styles';
import Tooltip from "@material-ui/core/Tooltip";

const useStylesOach = makeStyles((theme) => ({
    arrow: {
        color: theme.palette.common.black,
    },
    tooltip: {
        fontFamily: "Tele2 Slab Web Bold",
        fontSize: "14px",
        color: "#fff",
        maxWidth: "421px",
        alignSelf: "center",
        textShadow: "none",
        textAlign: "center",
        backgroundColor: theme.palette.common.black,
    },
}));

function OachInvoiceTooltip(props) {
    const classes = useStylesOach();  
    return <Tooltip arrow classes={classes} {...props} placement="top" interactive />;
}

export default class OachInvoice extends Component {
  constructor(props) {
    super(props);
    this.state = {
        account_hier_url: sessionData.account_hier_trans_params.RequestURL,
        account_hier_auth: sessionData.account_hier_trans_params.Authorization,
        invoice_url: sessionData.invoice_trans_params.RequestURL,
        invoice_auth: sessionData.invoice_trans_params.Authorization,
        oach_account_id: props.oach_account_id,
        oach_request_id: props.oach_request_id,
    };
    this.handleOpenInvoice = this.handleOpenInvoice.bind(this);
    this.openMenuDetails = this.openMenuDetails.bind(this);
    this.openMoreMenuDetails = this.openMoreMenuDetails.bind(this);
  }

  handleOpenInvoice(event) {
      window.open(event.target.getAttribute('invoice_url'), "_blank");
  }

  static getDerivedStateFromProps(nextProps, prevState) {
    if (nextProps.oach_account_id !== prevState.oach_account_id) {
        return {
            oach_account_id: nextProps.oach_account_id,
            oach_request_id: nextProps.oach_request_id
        };
    }
    return null;
  }

  componentDidUpdate(prevProps, prevState) {
    let invoices = [];
    let invoice = {};
    let billingAccountId = "";
    let a = this;
    if (this.state.oach_account_id && this.state.account_hier_url && this.state.invoice_url && prevState.oach_account_id !== this.state.oach_account_id) {
        let account_hier_url = this.state.account_hier_url.replace("<CustomerAccountId>", this.state.oach_account_id).replace("<Locale>", "LVI");
        axios.get(account_hier_url, {
            headers: {
            "Authorization": this.state.account_hier_auth,
            "X-Oach-Request-Id": this.state.oach_request_id
            }
        })
        .then(function (response) {
            if (response.status === 200) {
                for (let childAccount of response.data.children) {
                    if (childAccount.AccountClass === "Billing") {
                        billingAccountId = childAccount.id;
                    }
                }
                if (billingAccountId && a.state.invoice_url) {
                    let invoice_url = a.state.invoice_url.replace("<BillingAccountId>", billingAccountId).replace("<Locale>", "LVI");
                    axios.get(invoice_url, {
                        headers: {
                        "Authorization": a.state.invoice_auth,
                        "X-Oach-Request-Id": a.state.oach_request_id
                        }
                    })
                    .then(function (response) {
                        if (response.status === 200) {
                            for (let item of response.data) {
                                if (item.InvoiceType === "Standard") {
                                    invoice = {
                                        key: item.id,
                                        row_id: item.id,
                                        ba_id: item.InvoiceAccountId,
                                        ba_number: item.InvoiceAccountNumber,
                                        invoice_number: item.InvoiceNumber,
                                        invoice_bar_date: item.InvoiceLongDate,
                                        invoice_pop_date: item.InvoiceDate,
                                        invoice_due_date_label: item.DisputeOpenDate ? "" : item.DueAmount !== "0,00 €" ? "Due Date" : "",
                                        popup_due_date_label: item.DisputeOpenDate ? "" : item.DueAmount !== "0,00 €" ? "Due Date:" : "",
                                        invoice_due_date: item.DisputeOpenDate ? "" : item.DueAmount !== "0,00 €" ? item.DueDate : "",
                                        invoice_amount: item.InvoiceAmount,
                                        invoice_numeric_amount: item.InvoiceNumericAmount,
                                        invoice_due_amount: item.DueAmount,
                                        invoie_bar_icon_class: item.DisputeOpenDate ? "t2_inv_status_warning" : item.DueAmount !== "0,00 €" ? "t2_inv_status_important" : "t2_inv_status_ok",
                                        popup_header_class: item.DisputeOpenDate ? "In Dispute" : item.DueAmount !== "0,00 €" ? "Overdue" : "Paid",
                                        pdf_url: item.InvoiceURL,
                                    }
                                    invoices.push(invoice);
                                }
                            }
                            a.setState({
                                invoices: invoices,
                            });
                        }
                    })
                    .catch(function(error) {
                        console.error(error);
                    });
                }
            }
        })
        .catch(function(error) {
            console.error(error);
        });
    }
  }

  getInvoiceist() {
    let liItems;
    if (this.state.invoices !== undefined) {
        let invoices = this.state.invoices;
        let minInvoiceAmount = 99999;
        let maxInvoiceAmount = -99999;
        let minBarHeight = 45;
        let maxBarHeight = 75;
        for (const invoice of invoices) {
            if (Number(invoice.invoice_numeric_amount) < minInvoiceAmount) {
                minInvoiceAmount = Number(invoice.invoice_numeric_amount);
            }
            if (Number(invoice.invoice_numeric_amount) > maxInvoiceAmount) {
                maxInvoiceAmount = Number(invoice.invoice_numeric_amount);
            }
        }
        for (const invoice of invoices) {
            invoice.bar_height_percent = String(Math.round(((Number(invoice.invoice_numeric_amount) - minInvoiceAmount) / (maxInvoiceAmount - minInvoiceAmount)) * (maxBarHeight - minBarHeight)) + minBarHeight) + "%";
        }
        liItems = invoices.map((invoice) =>
            <li key={ invoice.key } className="regular nld" row_id={ invoice.invoice_number } ba_id={ invoice.ba_id } inv_type="Normal" ocr_nr={ invoice.invoice_number } tip_id={ invoice.row_id }>
                <div className="t2_col_header">
                    <span data-label="invoice_bar_date" className="t2_col_header_text t2_capitalize">{ invoice.invoice_bar_date }</span>
                </div>
                <div className="invoice-tip-target"/>
                <OachInvoiceTooltip key={ invoice.key } title={
                    <div className="t2_invoice_tooltip" style={{width: "421px", padding: "8px"}} invoice_id={ invoice.invoice_number }>
                        <div className="t2_inv_tooltip_line">
                            <div className="t2_inv_tooltip_title left_block">
                                <div t2_header_status={ invoice.popup_header_class }>Invoice</div>
                                <div t2_header_status={ invoice.popup_header_class }>-</div>
                                <div className="t2_capitalize">{ invoice.invoice_pop_date }</div>
                            </div>
                            <div data-label="invoice_tooltip_status" data-value={ invoice.invoie_bar_icon_class } className="t2_inv_tooltip_status right_block" style={{paddingRight: "0px"}} invstatus={ invoice.invoie_bar_icon_class }>
                                <div data-label="invoice_status" style={{width: "100%", display: "flex", flexDirection: "row-reverse", paddingRight: "0px"}}>
                                    <div style={{textAlign: "left", paddingRight: "0px"}}>{ invoice.popup_header_class }</div>
                                    <div className="t2_invoice_icon" style={{width: "16px", height: "24px", marginTop: "auto", paddingRight: "6px"}}></div>
                                </div>
                            </div>
                        </div>
                        <div className="t2_inv_tooltip_line">
                            <div className="left_block" style={{width: "48%"}}>
                                <div className="inv_tooltip_label">Billing Account #:</div>
                                <div data-label="Billing Account #">{ invoice.ba_number }</div>
                            </div>
                            <div className="right_block" style={{width: "52%"}}>
                                <div className="inv_tooltip_label" style={{paddingRight: "2px"}}>Invoice Amount:</div>
                                <div data-label="Invoice Amount">{ invoice.invoice_amount }</div>
                            </div>
                        </div>
                        <div className="t2_inv_tooltip_line">
                            <div className="left_block" style={{width: "48%"}}>
                                <div className="inv_tooltip_label">Invoice #:</div>
                                <div data-label="Invoice #"><a className="t2_invoice_ba ba_drilldown lvi_lth_eti" ba_id={ invoice.ba_id } invoice_id={ invoice.invoice_number }>{ invoice.invoice_number }</a></div>
                            </div>
                            <div className="right_block" style={{width: "52%"}}>
                                <div className="inv_tooltip_label" style={{paddingRight: "2px"}}>Outstanding Amount:</div>
                                <div data-label="Outstanding Amount">{ invoice.invoice_due_amount }</div>
                            </div>
                        </div>
                        <div className="t2_inv_tooltip_line">
                            <div className="left_block" style={{width: "48%"}}>
                                <div className="inv_tooltip_label">{ invoice.popup_due_date_label }</div>
                                <div data-label="Due Date">{ invoice.invoice_due_date }</div>
                            </div>
                        </div>
                        <div className="t2_inv_tooltip_line" style={{display: "block", textAlign: "center"}}>
                            <button style={{marginRight: "5px", marginLeft: "5px"}} onClick={this.handleOpenInvoice} className="t2_ouch_button" invoice_url={ invoice.pdf_url }>Open Invoice PDF</button>
                        </div>
                    </div>
                }>
                    <div draggable="true" invoice_nr={ invoice.invoice_number } ocr={ invoice.invoice_number } className="t2_invoice_bar regular" style={{height: invoice.bar_height_percent}} invstatus={ invoice.invoie_bar_icon_class }>
                        <div className="t2_bar_due_date">
                            <div>{ invoice.invoice_due_date_label }</div>
                            <div>{ invoice.invoice_due_date }</div>
                        </div>
                        <div data-label="invoice_bar_value" className="t2_bar_price">{ invoice.invoice_amount }</div>
                    </div>
                </OachInvoiceTooltip>
                <span data-label="invoice_bar_ba_nr" className="t2_invoice_number">
                    <a draggable="true" className="t2_invoice_ba t2_field_drilldown" ba_id={ invoice.ba_id }>{ invoice.ba_number }</a>
                </span>
            </li>
        );
    }
    return liItems;
  }

  openMenuDetails() {
    const currentState = this.state.menu_open;
    this.setState({ menu_open: !currentState });
  }

  openMoreMenuDetails() {
    const currentState = this.state.more_menu_open;
    this.setState({ more_menu_open: !currentState });
  }

  renderComponent() {
      if (this.state.oach_account_id) {
          return (
			<div id="t2_invoice_col_appl" className="t2_oach_applet t2_list_applet" applet_name="oach_invoices">
                <div className="t2_list_header">
                    <div className="t2_title">
                        <a id="t2_drilldown_acc_invoices" className="t2_drilldown_link">Invoices</a>
                    </div>
                    <div className="t2_search">
                        <input className="t2_filter_input" id="t2_invoices_search_inp" data-label="search" placeholder="Look for..." style={{width: "95%"}}></input>
                        <div id="t2_invoice_filter_option" className="filter-option"></div>
                    </div>
                    <div id="t2_menu_invoices" className="t2_menu_container">
                        <div className="t2_menu">
                            <div className="t2_menu_actions" onClick={this.openMenuDetails}></div>
                            <div className={ `t2_custom_menu t2_oach_scrollbar ${this.state.menu_open ? 't2_menu_toggled': null}` } style={{maxHeight: "150px"}}>
                                <div className="t2_custom_menu_item" id="t2_next_inv_adj">Create Next Invoice Adjustment</div>
                                <div className="t2_menu_more_actions" onClick={this.openMoreMenuDetails}>
                                    <span data-label="more_actions">More actions</span>
                                    <div className="t2_menu_arrow"><i className="fa fa-chevron-down rotate" aria-hidden="true"></i></div>
                                </div>
                                <div className={ `t2_common_menu ${this.state.more_menu_open ? 't2_menu_toggled': null}` }>
                                    <div className="t2_menu_common_item" action="menuExport">Export</div>
                                    <div className="t2_menu_common_item" action="menuCountRecords">Record count</div>
                                    <div className="t2_menu_common_item" action="menuAboutRecord">About record</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="t2_list_loader" id="t2_invoices_loader" style={{display: "none"}}>
                    <div className="t2_inner_loader">
                        <i className="fa fa-spinner fa-spin fa-lg fa-fw"></i>
                    Loading Invoices...</div>
                </div>
                <div className="jcarousel-wrapper" id="t2_invoice_carousel_wrapper" style={{display: "block"}}>
                    <div className="jcarousel" id="t2_invoice_jcarousel" data-jcarousel="true">
                        <ul style={{left: "0px", top: "0px"}}>
                            { this.getInvoiceist() }
                        </ul>
                    </div>
                    <a href="#" className="jcarousel-control-prev inactive" data-jcarouselcontrol="true" data-availability="disabled"></a>
                    <a href="#" className="jcarousel-control-next inactive" data-jcarouselcontrol="true" data-availability="disabled"></a>
                </div>
            </div>
          );
      } else {
          return <div style={{display: "none"}}></div>
      }
  }

  render() {
    return (
      this.renderComponent()
      );
    }
  }
  