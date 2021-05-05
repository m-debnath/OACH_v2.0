import React, { Component } from "react";
import axios from "axios";
import { makeStyles } from '@material-ui/core/styles';
import Tooltip from "@material-ui/core/Tooltip";
import tele2_black from "../../static/images/tele2_black.png";

const useStylesOach = makeStyles((theme) => ({
    arrow: {
        color: theme.palette.common.black,
    },
    tooltip: {
        fontFamily: "Tele2 Slab Web Bold",
        fontSize: "14px",
        color: "#fff",
        maxWidth: "400px",
        alignSelf: "center",
        textShadow: "none",
        textAlign: "center",
        backgroundColor: theme.palette.common.black,
    },
}));

function OachProductTooltip(props) {
    const classes = useStylesOach();  
    return <Tooltip arrow classes={classes} {...props} interactive />;
}

export default class OachProduct extends Component {
  constructor(props) {
    super(props);
    this.state = {
        asset_hier_url: sessionData.asset_hier_trans_params.RequestURL,
        asset_hier_auth: sessionData.asset_hier_trans_params.Authorization,
        oach_account_id: props.oach_account_id,
        oach_request_id: props.oach_request_id,
        menu_open: false,
        more_menu_open: false,
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
    let rootAssets = [];
    let rootAsset = {};
    let a = this;
    if (this.state.oach_account_id && this.state.asset_hier_url && prevState.oach_account_id !== this.state.oach_account_id) {
        let asset_hier_url = this.state.asset_hier_url.replace("<AccountId>", this.state.oach_account_id).replace("<AccountClass>", "Customer").replace("<Locale>", "LVI");
        axios.get(asset_hier_url, {
            headers: {
            "Authorization": this.state.asset_hier_auth,
            "X-Oach-Request-Id": this.state.oach_request_id
            }
        })
        .then(function (response) {
            if (response.status === 200) {
                for (let asset of response.data) {
                    rootAsset = {
                        key: asset.id,
                        row_id: asset.id,
                        integ_id: asset.AssetOrderItemId,
                        asset_pav: asset.PrimaryAttributeValue,
                        status: asset.Status,
                        status_color: asset.Status === "Active" ? "product-tooltip-row-status green" : "product-tooltip-row-status red",
                        status_class: asset.Status.toLowerCase(),
                        status_indc_class: "t2_product_" + asset.Status.toLowerCase(),
                        status_fa_class: asset.Status === "Active" ? "fa fa-check-circle product green" : "fa fa-times-circle product red",
                        tip_id: asset.id,
                        prod_indc_class: "t2_product_icon_" + (asset.ProductType === "Mobile Voice" ? "phone" : "globe"),
                        ba_id: asset.BillingAccountId,
                        ba_number: asset.BillingAccountNumber,
                        product_name: asset.Product,
                    }
                    rootAssets.push(rootAsset);
                }
                a.setState({
                    rootAssets: rootAssets,
                });
            }
        })
        .catch(function(error) {
            console.error(error);
        });
    }
  }

  getAssetList() {
    let liItems;
    if (this.state.rootAssets !== undefined) {
        liItems = this.state.rootAssets.map((rootAsset) =>
            <li key={ rootAsset.key } row_id={ rootAsset.row_id } integ_id={ rootAsset.integ_id } can_open="true" asset_pav={ rootAsset.asset_pav } className={ rootAsset.status_class } isvas="false" is_number_series="false" tip_id={ rootAsset.tip_id }>
                <OachProductTooltip key={ rootAsset.row_id } title={
                    <div className="products_opentip" id="product_opentip" style={{padding: "8px"}}>
                        <div className="product-tooltip-main" prod_id={ rootAsset.product_name }>
                            <div>
                                <div className="product-tooltip-row first" style={{ justifyContent: "space-between" }}>
                                    <div className="product-label" data-label="Number">{ rootAsset.asset_pav }</div>
                                    <div id="t2_tooltip_brand_div" className="t2_tooltip_brand">
                                        <div className="wsc_label">MyTele2 ADMIN</div>
                                    </div>
                                </div>
                                <div className="product-tooltip-block">
                                    <div className="product-tooltip-row">
                                        <div className="product-label">Password:</div>
                                        <div data-label="Password">Lauris</div>
                                    </div>
                                </div>
                                <div className="product-tooltip-block ">
                                    <div className={ rootAsset.status_color }>
                                        <i className={ rootAsset.status_fa_class } aria-hidden="true"></i>
                                        <span data-label="status">{ rootAsset.status }</span>
                                    </div>
                                    <div className="product-tooltip-row date">
                                        <div className="product-label">Product Name:</div>
                                        <div className="product-tooltip-grayish" data-label="Product Name">{ rootAsset.product_name }</div>
                                    </div>
                                </div>
                                <div className="product-tooltip-block">
                                    <div className="product-tooltip-row">
                                        <div className="product-label">Billing Account:</div>
                                        <div prod_id={ rootAsset.product_name } ba_id={ rootAsset.ba_id } className="ba_drilldown" data-label="Billing Account">{ rootAsset.ba_number }</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="product-tooltip-row">
                            <div value={ rootAsset.asset_pav } className="t2_ouch_button openIOTA">iOTA</div>
                        </div>
                        <div style={{position: "relative", left: 'calc(100% - 50px)', bottom: "21px", height: "0"}}>
                            <div style={{alignSelf: "flex-end", width: "10%"}}>
                                <img src={tele2_black} style={{width: "50px", minHeight: "12px", maxHheight: "20px"}}></img>
                                <div style={{display: "none"}}>tele2</div>                
                            </div>
                        </div>
                    </div>
                }>
                    <div className="t2_prod_container" style={{width: "129px"}}>
                        <div className="t2_prod_row">
                            <div className="t2_prod_icon">
                                <span className={ rootAsset.prod_indc_class }></span>
                            </div>
                            <div className="t2_prod_indc_col">
                                <div className="t2_prod_indc">
                                    <span className={ rootAsset.status_indc_class }></span>
                                </div>
                            </div>
                        </div>
                        <div draggable="true" className="t2_product_caption" ba_id={ rootAsset.ba_id } pav={ rootAsset.asset_pav } rootpav={ rootAsset.asset_pav }>
                            <div className="t2_product_name "><span data-label="Product Name">{ rootAsset.product_name }</span></div>
                            <div className="t2_product_prim_attr ">{ rootAsset.asset_pav }</div>
                        </div>
                    </div>
                </OachProductTooltip>
                <div className="t2_prod_container_1" style={{width: "1px", height:"1px"}}></div>
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
			<div id="t2_products_carousel_appl" className="t2_oach_applet t2_details_applet" applet_name="oach_products">
				<div id="t2_products_carousel_appl" className="t2_oach_applet t2_list_applet" applet_name="oach_products">
					<div className="t2_list_header">
						<div className="t2_title">
                        <a id="t2_drilldown_acc_assets" className="t2_drilldown_link">Assets</a>
                        </div>
						<div className="t2_search products asset">
							<input className="t2_filter_input products-search-with-filter" id="t2_products_search_inp" placeholder="Look for..." data-label="search" style={{width: "85%"}}></input>
							<div id="t2_assets_filter_option" className="filter-option filter-remove" style={{display: "none"}}></div>
						</div>
						<div id="t2_menu_products" className="t2_menu_container">
							<div className="t2_menu">
								<div className="t2_menu_actions" onClick={this.openMenuDetails}></div>
								<div className={ `t2_custom_menu ${this.state.menu_open ? 't2_menu_toggled': null}` }>
									<div className="t2_custom_menu_item" id="t2_open_sales_tool">Open Sales Tool</div>
									<div className="t2_custom_menu_item" id="t2_open_my_tele2_admins">Manage MyTele2 Admin</div>
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
					<div className="t2_list_loader" id="t2_products_loader" style={{display: "none"}}>
						<div className="t2_inner_loader">
							<i className="fa fa-spinner fa-spin fa-lg fa-fw"></i>
						</div>
					</div>
					<div className="jcarousel-wrapper" id="products_carousel_wrapper" style={{display: "block"}}>
						<div className="jcarousel" id="products_carousel" data-jcarousel="true">
							<ul style={{left: "0px", top: "0px"}}>
                            { this.getAssetList() }
							</ul>
						</div>
						<a href="#" className="jcarousel-control-prev inactive" data-jcarouselcontrol="true" data-availability="disabled"></a>
						<a href="#" className="jcarousel-control-next inactive" data-jcarouselcontrol="true" data-availability="disabled"></a>
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
  