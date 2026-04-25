import { useEffect, useState } from 'react';
import api from '../api';
import { PieChart, Pie, Cell, Tooltip, Legend } from 'recharts';

function Dashboard() {

    const [fields, setFields] = useState([]);
    const [stats, setStats] = useState(null);

    useEffect(() => {
        api.get('/fields/').then(res => setFields(res.data));
        api.get('/dashboard/stats/').then(res => setStats(res.data)).catch(() => {});
    }, []);
    
    const COLORS = { ACTIVE: '#22c55e', AT_RISK: '#eab308', COMPLETED: '#3b82f6' };
    const pieData = stats ? Object.entries(stats.status_breakdown).map(([k, v]) => ({ name: k, value: v })) : [];

    return (
        <div className="p-8">
            <h1 className="text-3xl mb-6">Field Monitoring Dashboard</h1>
            {stats && (
                <div className="grid grid-cols-4 gap-4 mb-8">
                    <div className="bg-white p-4 shadow rounded">
                        <p className="text-gray-500">Total Fields</p>
                        <p className="text-2xl font-bold">{stats.total_fields}</p>
                    </div>
                    <div className="bg-white p-4 shadow rounded col-span-2"> 
                        <p className="text-gray-500 mb-2">Status Breakdown</p>
                        <PieChart width={300} height={200}>
                            <Pie data={pieData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={60} label>

                            </Pie>
                            <Tooltip/>
                            <Legend/>
                        </PieChart>

                    </div>
                </div>
            )}

            <h2 className="text-xl mb-4">All Fields</h2>
            <table className="w-full bg-white shadow">
                <thead className="bg-gray-100">
                    <tr>
                        <th className="p-2 text-left">Name</th>
                        <th className="p-2 text-left">Crop</th>
                        <th className="p-2 text-left">Stage</th>
                        <th className="p-2 text-left">Status</th>
                        <th className="p-2 text-left">Agent</th>

                        
                        
                    </tr>
                </thead>
                <tbody>
                    {fields.map(f => (
                        <tr key={f.id} className="border-t">
                            <td className="p-2">{f.name}</td>
                            <td className="p-2">{f.crop_type}</td>
                            <td className="p-2">{f.current_stage}</td>
                            <td className="p-2">
                                <span className={`px-2 py-1 rounded text-white bg-[${COLORS[f.status]}]`}>
                                    {f.status}
                                </span>
                            </td>
                            <td className="p-2">{f.agent}</td>
                        </tr>
                    ))}    
                </tbody>
            </table>



        </div>
          
    );
}

export default Dashboard