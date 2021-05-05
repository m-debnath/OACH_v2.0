import React, { Component } from "react";
import axios from "axios";

export default class OachOrder extends Component {
  constructor(props) {
    super(props);
    this.state = {
        order_hier_url: sessionData.order_hier_trans_params.RequestURL,
        order_hier_auth: sessionData.order_hier_trans_params.Authorization,
        oach_account_id: props.oach_account_id,
        oach_request_id: props.oach_request_id,
    };
    this.openMenuDetails = this.openMenuDetails.bind(this);
    this.openMoreMenuDetails = this.openMoreMenuDetails.bind(this);
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
    let orders = [];
    let order = {};
    let a = this;
    if (this.state.oach_account_id && this.state.order_hier_url && prevState.oach_account_id !== this.state.oach_account_id) {
        let order_hier_url = this.state.order_hier_url.replace("<AccountId>", this.state.oach_account_id).replace("<AccountClass>", "Customer").replace("<Locale>", "LVI");
        axios.get(order_hier_url, {
            headers: {
            "Authorization": this.state.order_hier_auth,
            "X-Oach-Request-Id": this.state.oach_request_id
            }
        })
        .then(function (response) {
            if (response.status === 200) {
                for (const [i, item] of response.data.entries()) {
                    order = {
                        key: item.id,
                        row_id: item.id,
                        order_date: item.OrderDate,
                        order_type: item.Type,
                        status: item.Status,
                        ba_number: item.BillingAccountNumber,
                        order_number: item.OrderNumber,
                        row_class: (i % 2 === 0 ? "odd" : "even") + (item.Status === "In Progress" ? " status_in_progress" : ""),
                        td_class: item.Status === "In Progress" ? "status_in_progress" : "",
                    }
                    orders.push(order);
                }
                a.setState({
                    orders: orders,
                });
            }
        })
        .catch(function(error) {
            console.error(error);
        });
    }
  }

  getOrderList() {
    let trItems;
    if (this.state.orders !== undefined) {
        trItems = this.state.orders.map((order) =>
            <tr key={ order.key } role="row" className={ order.row_class } row_id={ order.row_id } data-index="0">
                <td data-text={ order.order_date } data-label="Order Date" className={ order.td_class }><div className="order_no_overflow"><span className="t2_order_selector"></span>{ order.order_date }</div></td>
                <td data-text={ order.order_type } data-label="Order Type" className={ order.td_class }><div className="order_no_overflow">{ order.order_type }</div></td>
                <td data-text={ order.status } data-label="Status" className={ order.td_class }><div className="order_no_overflow">{ order.status }</div></td>
                <td className="t2_field_drilldown" data-text={ order.ba_number } data-label="Billing Account" className={ order.td_class }><div className="order_no_overflow"><a className="orderbanr t2_field_drilldown">{ order.ba_number }</a></div></td>
                <td className="t2_field_drilldown" data-text={ order.order_number } data-label="Order #" className={ order.td_class }><div className="order_no_overflow"><a className="ordernr t2_field_drilldown">{ order.order_number }</a></div></td>
            </tr>
        );
    }
    return trItems;
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
			<div id="t2_orders_list_appl" className="t2_oach_applet t2_list_applet" applet_name="oach_orders">
                <div className="t2_list_header">
                    <div className="t2_title">
                        <a id="t2_drilldown_acc_orders" className="t2_drilldown_link" drilldown="Account Detail - Orders View;;Account;;Account;;1-4X1RC1">Orders</a>
                    </div>
                    <div className="t2_search">
                        <input className="t2_filter_input" id="t2_orders_search_inp" data-label="search" placeholder="Look for..."></input>
                    </div>
                    <div id="t2_menu_orders" className="t2_menu_container">
                        <div className="t2_menu">
                            <div className="t2_menu_actions" onClick={this.openMenuDetails}></div>
                            <div className={ `t2_custom_menu ${this.state.menu_open ? 't2_menu_toggled': null}` }>
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
                <div className="t2_list_loader" id="t2_orders_loader" style={{display: "none"}}>
                    <div className="t2_inner_loader">
                        <i className="fa fa-spinner fa-spin fa-lg fa-fw"></i>
                    Loading Orders...</div>
                </div>
                <div className="t2_applet_main">
                    <div id="t2_orders_table_wrapper" className="dataTables_wrapper no-footer">
                        <table id="t2_orders_table" className="t2_list_table dataTable no-footer" role="grid" style={{display: "table"}}>
                            <thead>
                                <tr role="row">
                                    <th className="sorting_disabled" rowSpan="1" colSpan="1">Order Date</th>
                                    <th className="sorting_disabled" rowSpan="1" colSpan="1" style={{width: "25%"}}>Order Type</th>
                                    <th className="sorting_disabled" rowSpan="1" colSpan="1">Status</th>
                                    <th className="sorting_disabled" rowSpan="1" colSpan="1" style={{width: "24%"}}>Billing Account</th>
                                    <th className="sorting_disabled" rowSpan="1" colSpan="1">Order #</th>
                                </tr>
                            </thead>
                            <tbody>
                                { this.getOrderList() }
                            </tbody>
                        </table>
                    </div>
                    <div className="list_nav">
                        <div className="prev_page btn_disabled" data-availability="disabled"></div>
                        <div className="next_page btn_disabled" data-availability="disabled"></div>
                    </div>
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
  