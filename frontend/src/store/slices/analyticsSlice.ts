import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import api from '../../services/api'

interface Analytics {
  totalPortfolioValue: number
  activeProjects: number
  totalWip: number
  averageMargin: number
  invoicingStatusSummary: any
}

interface AnalyticsState {
  data: Analytics | null
  loading: boolean
  error: string | null
}

const initialState: AnalyticsState = {
  data: null,
  loading: false,
  error: null,
}

export const fetchAnalytics = createAsyncThunk(
  'analytics/fetchAnalytics',
  async (_, { rejectWithValue }) => {
    try {
      const response = await api.get('/v1/analytics/dashboard')
      return response.data
    } catch (error: any) {
      return rejectWithValue(error.response?.data?.detail || 'Failed to fetch analytics')
    }
  }
)

const analyticsSlice = createSlice({
  name: 'analytics',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchAnalytics.pending, (state) => {
        state.loading = true
        state.error = null
      })
      .addCase(fetchAnalytics.fulfilled, (state, action) => {
        state.loading = false
        state.data = action.payload
      })
      .addCase(fetchAnalytics.rejected, (state, action) => {
        state.loading = false
        state.error = action.payload as string
      })
  },
})

export default analyticsSlice.reducer
