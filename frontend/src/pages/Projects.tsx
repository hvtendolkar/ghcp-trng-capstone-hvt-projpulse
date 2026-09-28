import React, { useEffect, useState } from 'react'
import { useAppDispatch, useAppSelector } from '../store/hooks'
import { fetchProjects, createProject } from '../store/slices/projectsSlice'
import { Plus, Edit2, Trash2 } from 'lucide-react'

function Projects() {
  const dispatch = useAppDispatch()
  const { projects, loading } = useAppSelector((state) => state.projects)
  const [showForm, setShowForm] = useState(false)
  const [formData, setFormData] = useState({
    name: '',
    code: '',
    status: 'Active',
    engagement_type: 'Time & Material',
    budget: '',
  })

  useEffect(() => {
    dispatch(fetchProjects())
  }, [dispatch])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    dispatch(createProject(formData))
    setFormData({ name: '', code: '', status: 'Active', engagement_type: 'Time & Material', budget: '' })
    setShowForm(false)
  }

  if (loading) {
    return <div className="p-6">Loading projects...</div>
  }

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-gray-900">Projects</h1>
        <button
          onClick={() => setShowForm(!showForm)}
          className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
        >
          <Plus size={20} />
          New Project
        </button>
      </div>

      {showForm && (
        <div className="bg-white rounded-lg shadow p-6 mb-6">
          <h2 className="text-lg font-semibold mb-4">Create New Project</h2>
          <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4">
            <input
              type="text"
              placeholder="Project Name"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />
            <input
              type="text"
              placeholder="Project Code"
              value={formData.code}
              onChange={(e) => setFormData({ ...formData, code: e.target.value })}
              className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />
            <select
              value={formData.engagement_type}
              onChange={(e) => setFormData({ ...formData, engagement_type: e.target.value })}
              className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option>Time & Material</option>
              <option>Fixed-Cost</option>
              <option>Retainer</option>
            </select>
            <input
              type="number"
              placeholder="Budget"
              value={formData.budget}
              onChange={(e) => setFormData({ ...formData, budget: e.target.value })}
              className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              type="submit"
              className="col-span-2 bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition"
            >
              Create Project
            </button>
          </form>
        </div>
      )}

      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50 border-b border-gray-200">
            <tr>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Name</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Code</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Status</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Type</th>
              <th className="px-6 py-3 text-left text-sm font-semibold text-gray-900">Margin</th>
              <th className="px-6 py-3 text-right text-sm font-semibold text-gray-900">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {projects.length === 0 ? (
              <tr>
                <td colSpan={6} className="px-6 py-8 text-center text-gray-500">
                  No projects yet. Create one to get started.
                </td>
              </tr>
            ) : (
              projects.map((project) => (
                <tr key={project.project_id} className="hover:bg-gray-50">
                  <td className="px-6 py-4 text-sm font-medium text-gray-900">{project.name}</td>
                  <td className="px-6 py-4 text-sm text-gray-600">{project.code}</td>
                  <td className="px-6 py-4 text-sm">
                    <span className="inline-flex items-center px-2 py-1 rounded-lg bg-green-100 text-green-800 text-xs font-semibold">
                      {project.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600">{project.engagement_type}</td>
                  <td className="px-6 py-4 text-sm font-semibold text-gray-900">{project.margin}%</td>
                  <td className="px-6 py-4 text-right text-sm space-x-2">
                    <button className="inline-flex items-center gap-1 px-2 py-1 text-blue-600 hover:text-blue-700">
                      <Edit2 size={16} />
                    </button>
                    <button className="inline-flex items-center gap-1 px-2 py-1 text-red-600 hover:text-red-700">
                      <Trash2 size={16} />
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default Projects
