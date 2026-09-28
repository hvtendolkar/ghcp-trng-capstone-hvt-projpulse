import React from 'react'
import { PieChart, Pie, Cell, ResponsiveContainer, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts'

function Analytics() {
  const wipData = [
    { name: '0-30 days', value: 150000, fill: '#10b981' },
    { name: '31-60 days', value: 180000, fill: '#f59e0b' },
    { name: '61-90 days', value: 95000, fill: '#ef4444' },
  ]

  const marginData = [
    { project: 'A', margin: 38, target: 40 },
    { project: 'B', margin: 42, target: 40 },
    { project: 'C', margin: 36, target: 40 },
    { project: 'D', margin: 41, target: 40 },
  ]

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Financial Analytics</h1>

      <div className="grid grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">WIP Aging Analysis</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={wipData}
                cx="50%"
                cy="50%"
                labelLine={false}
                label={({ name, value }) => `${name}: $${value / 1000}K`}
                outerRadius={100}
                fill="#8884d8"
                dataKey="value"
              >
                {wipData.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={entry.fill} />
                ))}
              </Pie>
            </PieChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Margin vs Target</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={marginData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="project" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="margin" stroke="#3b82f6" strokeWidth={2} name="Actual" />
              <Line type="monotone" dataKey="target" stroke="#10b981" strokeWidth={2} name="Target" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Key Metrics</h3>
        <div className="grid grid-cols-4 gap-4">
          <div className="text-center p-4">
            <p className="text-gray-600 text-sm">Invoicing %</p>
            <p className="text-2xl font-bold text-gray-900 mt-2">82.5%</p>
          </div>
          <div className="text-center p-4">
            <p className="text-gray-600 text-sm">Collection Rate</p>
            <p className="text-2xl font-bold text-gray-900 mt-2">94.2%</p>
          </div>
          <div className="text-center p-4">
            <p className="text-gray-600 text-sm">Avg Days to Invoice</p>
            <p className="text-2xl font-bold text-gray-900 mt-2">12.5</p>
          </div>
          <div className="text-center p-4">
            <p className="text-gray-600 text-sm">Budget Utilization</p>
            <p className="text-2xl font-bold text-gray-900 mt-2">87.3%</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Analytics
