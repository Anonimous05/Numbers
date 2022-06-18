import React from 'react';
import './styles.css'

const Index = (props) => {

    const {
        orders
    } = props;

    return (
        <div className='table_main_container'>
            <div className='table_container'>
                <div className="titles">
                    <div>Заказ №</div>
                    <div>Стоимость $</div>
                    <div>Стоимость ₽</div>
                    <div>Срок Поставки</div>
                </div>
                <div className="table_rows">
                    {orders?.map(order => (
                        <div className="table_row" key={order.id}>
                            <div>{order.order_number}</div>
                            <div>{order.price_usd}</div>
                            <div>{order.price_rub.toFixed(2)}</div>
                            <div><b>{order.delivery_date}</b></div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default Index;