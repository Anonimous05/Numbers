import React, {Component} from 'react';
import './App.css'
import {AxiosAPI} from "./AxiosAPI";
import OrdersTable from "./Components/OrdersTable";
import OrdersChart from "./Components/OrdersChart";

class App extends Component {

    state = {
        orders: null,
        currency: 'usd'
    }

    async componentDidMount() {
        try {
            const {data} = await AxiosAPI.get('orders/');

            this.setState({
                orders: data
            });
        } catch (error) {
            console.log(error)
        }
    }

    onChangeSelect = (e) => {
        this.setState({
            [e.target.name]: e.target.value
        })
    }

    render() {
        return (
            <div className='App'>
                {this.state.orders?.length > 0 && (
                    <div>
                        <div className="head">
                            <div className="select">
                                <p>Select Currency</p>
                                <select name="currency" onChange={this.onChangeSelect}>
                                    <option value="usd">USD</option>
                                    <option value="rub">RUB</option>
                                </select>
                            </div>
                            <div className="total">
                                <h3>Total Price $</h3>
                                <p>
                                    {this.state.orders.map(order => order[`price_${this.state.currency}`])
                                        .reduce((a, b) => a + b).toFixed(0)}
                                </p>
                            </div>
                        </div>
                        <div style={{display: 'flex'}}>
                            <OrdersTable orders={this.state.orders}/>
                            <OrdersChart orders={this.state.orders} currency={this.state.currency}/>
                        </div>
                    </div>
                )}
            </div>
        );
    }
}

export default App;