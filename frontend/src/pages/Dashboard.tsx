import React, { useEffect } from 'react'
import { useAppDispatch, useAppSelector } from '../store/hooks'
import { fetchAnalytics } from '../store/slices/analyticsSlice'
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { TrendingUp, AlertCircle, Zap } from 'lucide-react'

function Dashboard() {
  const dispatch = useAppDispatch()
  const { data, loading } = useAppSelector((state) => state.analytics)

  useEffect(() => {
    dispatch(fetchAnalytics())
  }, [dispatch])

  if (loading) {
    return <div className="p-6 text-center">Loading dashboard...</div>
  }

  // Format currency values
  const formatCurrency = (value: string | number) => {
    const num = typeof value === 'string' ? parseFloat(value) : value
    if (isNaN(num)) return '$0'
    if (num >= 1000000) return `$${(num / 1000000).toFixed(1)}M`
    if (num >= 1000) return `$${(num / 1000).toFixed(0)}K`
    return `$${num.toFixed(0)}`
  }

  const mockChartData = [
    { month: 'Jan', wip: 150000, revenue: 250000, margin: 40 },
    { month: 'Feb', wip: 160000, revenue: 270000, margin: 38 },
    { month: 'Mar', wip: 145000, revenue: 280000, margin: 42 },
    { month: 'Apr', wip: 170000, revenue: 300000, margin: 41 },
    { month: 'May', wip: 155000, revenue: 290000, margin: 39 },
    { month: 'Jun', wip: 140000, revenue: 310000, margin: 43 },
  ]

  const mockProjectData = [
    { name: 'Project A', value: 45, margin: 38 },
    { name: 'Project B', value: 30, margin: 42 },
    { name: 'Project C', value: 25, margin: 36 },
  ]

  return (
    <div className="p-6 space-y-6">
      <div className="grid grid-cols-4 gap-4">
        {/* KPI Cards */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-500 text-sm font-medium">Portfolio Value</p>
              <p className="text-2xl font-bold text-gray-900 mt-2">{data ? formatCurrency(data.total_portfolio_value) : '$0'}</p>
            </div>
            <div className="bg-blue-100 p-3 rounded-lg">
              <TrendingUp className="text-blue-600" size={24} />
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-500 text-sm font-medium">Active Projects</p>
              <p className="text-2xl font-bold text-gray-900 mt-2">{data ? data.active_projects : 0}</p>
            </div>
            <div className="bg-green-100 p-3 rounded-lg">
              <TrendingUp className="text-green-600" size={24} />
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-500 text-sm font-medium">Total WIP</p>
              <p className="text-2xl font-bold text-gray-900 mt-2">{data ? formatCurrency(data.total_wip) : '$0'}</p>
            </div>
            <div className="bg-yellow-100 p-3 rounded-lg">
              <AlertCircle className="text-yellow-600" size={24} />
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-500 text-sm font-medium">Avg Margin</p>
              <p className="text-2xl font-bold text-gray-900 mt-2">{data ? `${data.average_margin.toFixed(1)}%` : '0%'}</p>
            </div>
            <div className="bg-purple-100 p-3 rounded-lg">
              <Zap className="text-purple-600" size={24} />
            </div>
          </div>
        </div>
      </div>

      {/* Charts */}
      <div className="grid grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">WIP & Revenue Trend</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={mockChartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="wip" stroke="#3b82f6" strokeWidth={2} />
              <Line type="monotone" dataKey="revenue" stroke="#10b981" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Project Margin Distribution</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={mockProjectData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="margin" fill="#8b5cf6" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* AI Insights */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">AI Insights & Alerts</h3>
        <div className="space-y-3">
          <div className="flex items-start gap-3 p-3 bg-red-50 rounded-lg">
            <AlertCircle className="text-red-600 flex-shrink-0 mt-0.5" size={18} />
            <div>
              <p className="font-medium text-red-900">Critical: High WIP Aging</p>
              <p className="text-sm text-red-700">Project A has 3 invoices over 60 days old totaling $125K</p>
            </div>
          </div>

          <div className="flex items-start gap-3 p-3 bg-yellow-50 rounded-lg">
            <AlertCircle className="text-yellow-600 flex-shrink-0 mt-0.5" size={18} />
            <div>
              <p className="font-medium text-yellow-900">Warning: Margin Erosion</p>
              <p className="text-sm text-yellow-700">Project C margin dropped 4% this month. Recommend resource review.</p>
            </div>
          </div>

          <div className="flex items-start gap-3 p-3 bg-blue-50 rounded-lg">
            <Zap className="text-blue-600 flex-shrink-0 mt-0.5" size={18} />
            <div>
              <p className="font-medium text-blue-900">Recommendation: Optimize Billing</p>
              <p className="text-sm text-blue-700">Consider shifting Project B to milestone-based invoicing to improve cash flow.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
