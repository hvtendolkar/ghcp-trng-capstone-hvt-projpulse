import React from 'react'
import { Link, useLocation } from 'react-router-dom'
import {
  BarChart3,
  Briefcase,
  Users,
  FileText,
  Settings as SettingsIcon,
  LayoutDashboard,
} from 'lucide-react'

function Sidebar() {
  const location = useLocation()

  const navItems = [
    { icon: LayoutDashboard, label: 'Dashboard', href: '/' },
    { icon: Briefcase, label: 'Projects', href: '/projects' },
    { icon: Users, label: 'Resources', href: '/resources' },
    { icon: BarChart3, label: 'Analytics', href: '/analytics' },
    { icon: FileText, label: 'Invoices', href: '/invoices' },
    { icon: SettingsIcon, label: 'Settings', href: '/settings' },
  ]

  return (
    <div className="w-64 bg-gray-900 text-white flex flex-col">
      <div className="p-6 border-b border-gray-800">
        <h2 className="text-xl font-bold">ProjectPulse</h2>
        <p className="text-xs text-gray-400 mt-1">Financial Analytics</p>
      </div>

      <nav className="flex-1 px-4 py-6 space-y-2">
        {navItems.map((item) => {
          const Icon = item.icon
          const isActive = location.pathname === item.href
          return (
            <Link
              key={item.href}
              to={item.href}
              className={`flex items-center gap-3 px-4 py-3 rounded-lg transition ${
                isActive
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-300 hover:bg-gray-800 hover:text-white'
              }`}
            >
              <Icon size={20} />
              <span>{item.label}</span>
            </Link>
          )
        })}
      </nav>

      <div className="p-4 border-t border-gray-800 text-xs text-gray-400">
        <p>v1.0.0</p>
      </div>
    </div>
  )
}

export default Sidebar
