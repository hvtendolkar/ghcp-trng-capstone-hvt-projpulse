import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import api from '../../services/api'

interface Project {
  project_id: string
  name: string
  code: string
  status: string
  engagement_type: string
  margin: number
  wip: number
  invoicing_status: string
  created_at: string
}

interface ProjectsState {
  projects: Project[]
  loading: boolean
  error: string | null
  selectedProject: Project | null
}

const initialState: ProjectsState = {
  projects: [],
  loading: false,
  error: null,
  selectedProject: null,
}

export const fetchProjects = createAsyncThunk(
  'projects/fetchProjects',
  async (_, { rejectWithValue }) => {
    try {
      const response = await api.get('/api/v1/projects')
      return response.data
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch projects')
    }
  }
)

export const createProject = createAsyncThunk(
  'projects/createProject',
  async (projectData: any, { rejectWithValue }) => {
    try {
      const response = await api.post('/api/v1/projects', projectData)
      return response.data
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to create project')
    }
  }
)

const projectsSlice = createSlice({
  name: 'projects',
  initialState,
  reducers: {
    selectProject: (state, action) => {
      state.selectedProject = action.payload
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchProjects.pending, (state) => {
        state.loading = true
        state.error = null
      })
      .addCase(fetchProjects.fulfilled, (state, action) => {
        state.loading = false
        state.projects = action.payload.items
      })
      .addCase(fetchProjects.rejected, (state, action) => {
        state.loading = false
        state.error = action.payload as string
      })
      .addCase(createProject.pending, (state) => {
        state.loading = true
      })
      .addCase(createProject.fulfilled, (state, action) => {
        state.loading = false
        state.projects.push(action.payload)
      })
      .addCase(createProject.rejected, (state, action) => {
        state.loading = false
        state.error = action.payload as string
      })
  },
})

export const { selectProject } = projectsSlice.actions
export default projectsSlice.reducer
