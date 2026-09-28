import React from 'react'

function Invoices() {
  const invoices = [
    { id: 'INV001', project: 'Project A', amount: 45000, status: 'Paid', dueDate: '2026-09-30' },
    { id: 'INV002', project: 'Project B', amount: 38000, status: 'Sent', dueDate: '2026-10-15' },
    { id: 'INV003', project: 'Project C', amount: 52000, status: 'Draft', dueDate: '2026-10-30' },
  ]

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'Paid':
        return 'bg-green-100 text-green-800'
      case 'Sent':
        return 'bg-blue-100 text-blue-800'
      default:
        return 'bg-gray-100 text-gray-800'
    }
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Invoice Management</h1>

      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50 border-b border-gray-200">
            <tr>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Invoice #</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Project</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Amount</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Due Date</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Status</th>
              <th className="px-6 py-3 text-right text-sm font-semibold text-gray-900">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {invoices.map((invoice) => (
              <tr key={invoice.id} className="hover:bg-gray-50">
                <td className="px-6 py-4 text-sm font-medium text-gray-900">{invoice.id}</td>
                <td className="px-6 py-4 text-sm text-gray-600">{invoice.project}</td>
                <td className="px-6 py-4 text-sm font-semibold text-gray-900">${invoice.amount.toLocaleString()}</td>
                <td className="px-6 py-4 text-sm text-gray-600">{invoice.dueDate}</td>
                <td className="px-6 py-4 text-sm">
                  <span className={`inline-flex items-center px-2 py-1 rounded-lg text-xs font-semibold ${getStatusColor(invoice.status)}`}>
                    {invoice.status}
                  </span>
                </td>
                <td className="px-6 py-4 text-right text-sm space-x-2">
                  <button className="text-blue-600 hover:text-blue-700 font-medium">View</button>
                  <button className="text-gray-600 hover:text-gray-700 font-medium">Download</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default Invoices
