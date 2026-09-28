import React from 'react'

function Resources() {
  const resources = [
    { id: 1, name: 'John Smith', designation: 'Senior Manager', rate: 350, projects: 3 },
    { id: 2, name: 'Sarah Johnson', designation: 'Manager', rate: 280, projects: 2 },
    { id: 3, name: 'Mike Chen', designation: 'Consultant', rate: 200, projects: 4 },
  ]

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-900 mb-6">Resource Management</h1>

      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50 border-b border-gray-200">
            <tr>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Name</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Designation</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Billable Rate</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Projects Assigned</th>
              <th className="px-6 py-3 text-right text-sm font-semibold text-gray-900">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {resources.map((resource) => (
              <tr key={resource.id} className="hover:bg-gray-50">
                <td className="px-6 py-4 text-sm font-medium text-gray-900">{resource.name}</td>
                <td className="px-6 py-4 text-sm text-gray-600">{resource.designation}</td>
                <td className="px-6 py-4 text-sm font-semibold text-gray-900">${resource.rate}/hr</td>
                <td className="px-6 py-4 text-sm text-gray-600">{resource.projects}</td>
                <td className="px-6 py-4 text-right text-sm space-x-2">
                  <button className="text-blue-600 hover:text-blue-700 font-medium">Edit</button>
                  <button className="text-red-600 hover:text-red-700 font-medium">Delete</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default Resources
