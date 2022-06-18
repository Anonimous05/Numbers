import React from 'react';
import {Line} from 'react-chartjs-2';
import {
    CategoryScale,
    Chart as ChartJS,
    LinearScale,
    LineElement,
    PointElement,
    Tooltip,
} from "chart.js";

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Tooltip
);

const Index = (props) => {

    const {
        orders,
        currency
    } = props;

    const options = {
        responsive: true
    };

    const labels = orders.map(order => order.delivery_date);

    const getData = () => {
        return {
            labels,
            datasets: [
                {
                    data: labels.map((label, index) => orders[index][`price_${currency}`]),
                    borderColor: '#64c8ff',
                    backgroundColor: 'transparent',
                }
            ],
        };
    }

    return (
        <div style={{display: 'flex', justifyContent: 'center', width: '50%', alignItems: 'center', padding: 10}}>
            <Line data={getData()} options={options} type={'line'}/>
        </div>
    );
};

export default Index;